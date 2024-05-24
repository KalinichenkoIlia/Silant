from django.contrib.auth import authenticate
from django.shortcuts import render

from allauth.account.views import LoginView, LogoutView
from requests import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import viewsets
from .serializers import userSerializers
from django.contrib.auth.models import User


class AccountLoginView(LoginView):
    template_name = "custom_login.html"


class UserViewSets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializers
