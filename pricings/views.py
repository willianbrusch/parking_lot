from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import PriceSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Price


class PriceView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.is_superuser == True:
            serializer = PriceSerializer(data=request.data)

            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            price = Price.objects.create(**request.data)
            serializer = PriceSerializer(price)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
