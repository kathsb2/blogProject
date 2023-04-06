from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework import status
from rest_framework import serializers

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserRegisterSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status = status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': {},
                'message': 'Signup Successful!',
            }, status = status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserLoginSerializer(data = data)

            if not serializer.is_valid():
                return Response({
                    'data': serializer.errors,
                    'message': 'Something went wrong',
                }, status = status.HTTP_400_BAD_REQUEST)

            response = serializer.get_jwt_token(serializer.data)

            return Response(response, status = status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'data': {},
                'message': 'Something went wrong',
            }, status = status.HTTP_400_BAD_REQUEST)
