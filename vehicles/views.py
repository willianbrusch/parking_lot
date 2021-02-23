from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import VehicleSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Vehicle
from pricings.models import Price
from levels.models import Level
from vehicles.models import Vehicle
from datetime import datetime, timezone


class VehicleView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_superuser == True:
            price = Price.objects.all()

            if not price:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:

                levels = Level.objects.all().order_by('fill_priority')

                if not levels:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                else:

                    for level in levels:
                        level_active = ''

                        if request.data['vehicle_type'] == 'car':
                            if level.car_spots > 0:
                                Level.objects.filter(
                                    id=level.id).update(car_spots=level.car_spots - 1)
                                level_active = level
                                break

                        if request.data['vehicle_type'] == 'bike':
                            if level.bike_spots > 0:
                                Level.objects.filter(
                                    id=level.id).update(bike_spots=level.bike_spots - 1)
                                level_active = level
                                break

                        if level == levels[len(levels)-1]:
                            return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = VehicleSerializer(data=request.data)

                if not serializer.is_valid():
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                vehicle = Vehicle.objects.create(**request.data)

                Vehicle.objects.filter(
                    id=vehicle.id).update(variety=vehicle.vehicle_type, level_name=level_active.name, level_id=level_active.id)

                new_response = {}
                new_response['id'] = vehicle.id
                new_response['vehicle_type'] = vehicle.vehicle_type
                new_response['license_plate'] = vehicle.license_plate
                new_response['arrived_at'] = vehicle.arrived_at
                new_response['paid_at'] = vehicle.paid_at
                new_response['amount_paid'] = vehicle.amount_paid
                new_response['spot'] = {
                    'id': level_active.id,
                    'variety': vehicle.vehicle_type,
                    'level_name': level_active.name
                }

                return Response(new_response, status=status.HTTP_201_CREATED)

    def put(self, request, vehicle_id):
        if request.user.is_superuser == True:

            try:
                vehicle = Vehicle.objects.get(id=vehicle_id)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)

            paid_at = datetime.now(timezone.utc)
            time = paid_at - vehicle.arrived_at
            price = Price.objects.first()

            time = int(time.seconds)/3600

            if time <= 1:
                time = 1

            value = price.a_coefficient + (price.b_coefficient * time)
            value = value / time

            Vehicle.objects.filter(id=vehicle_id).update(paid_at=paid_at)

            Vehicle.objects.filter(id=vehicle_id).update(
                amount_paid=value)

            level = Level.objects.get(id=vehicle.level_id)

            if vehicle.vehicle_type == 'car':
                Level.objects.filter(
                    id=vehicle.level_id).update(car_spots=level.car_spots + 1)

            if vehicle.vehicle_type == 'bike':
                Level.objects.filter(id=vehicle.level_id).update(
                    bike_spots=level.bike_spots + 1)

            new_response = {}
            new_response['id'] = vehicle.id
            new_response['vehicle_type'] = vehicle.vehicle_type
            new_response['license_plate'] = vehicle.license_plate
            new_response['arrived_at'] = vehicle.arrived_at
            new_response['paid_at'] = paid_at
            new_response['amount_paid'] = value
            new_response['spot'] = None

            return Response(new_response, status=status.HTTP_200_OK)
