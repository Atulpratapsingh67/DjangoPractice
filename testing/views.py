from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from testing.serializer import UserSerializer


user = get_user_model()

class Test(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']
    queryset = user.objects.all()
    serializer_class = UserSerializer