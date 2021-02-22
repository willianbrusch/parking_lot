from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LevelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Level


class LevelView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_superuser == True:
            serializer = LevelSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            level = Level.objects.create(**request.data)

            new_response = {}
            new_response['id'] = level.id
            new_response['name'] = level.name
            new_response['fill_priority'] = level.fill_priority
            new_response['available_spots'] = {
                'available_bike_spots': level.bike_spots,
                'available_car_spots': level.car_spots
            }

            return Response(new_response, status=status.HTTP_201_CREATED)

    def get(self, request):
        allLevels = Level.objects.all()

        all_levels_array = []

        for level in allLevels:
            new_response = {}

            new_response['id'] = level.id
            new_response['name'] = level.name
            new_response['fill_priority'] = level.fill_priority
            new_response['available_spots'] = {
                'available_bike_spots': level.bike_spots,
                'available_car_spots': level.car_spots
            }

            all_levels_array.append(new_response)

        return Response(all_levels_array)
