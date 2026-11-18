from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from account.models import User
from account.serializer import RegisterSerializer, LoginSerilaizer, VarifyOTPCodeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .models import OTPCode
import random
from django.core.mail import send_mail
from rest_framework import status
from project.settings import EMAIL_HOST_USER

class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            code = str(random.randint(100000, 999999))

            OTPCode.objects.filter(email=email).delete()
    
            OTPCode.objects.create(email=email, code=code)

            send_mail(
                subject='ваш код подверждения',
                message = f'Ваш код : {code}',
                from_email = EMAIL_HOST_USER,
                recipient_list = [email]
            )

            return Response({'message' : 'мы отправили код'})
        
        return Response(
            serializer.errors,
            status=status.HTTP_401_UNAUTHORIZED
            )
    
class VerifyCode(APIView):
    def post(self, request):
        serializer = VarifyOTPCodeSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            otp = serializer.validated_data['otp']
            phone = serializer.validated_data['phone']

            user = User.objects.create_user(
                email=email,
                username=email,
                password=password,
                phone = phone
            )

            {
            "email":"abdykarow@gmail.com",
            "password":"12345678",
            "code":"429934",
            "phone":"+996700700777"
            }

            otp.delete()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'User was created with token',
                'token': token.key
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    


class Login(APIView):
    def post(self, request):
        serializer = LoginSerilaizer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            token, created = Token.objects.get_or_create(user = user)

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class Logout(APIView):
    def post(self, request):
        Token.objects.get(user=request.user).delete()

        return Response({'message' : 'logout successful'})