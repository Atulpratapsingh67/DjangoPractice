from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from testing.serializer import UserSerializer
import requests

user = get_user_model()

class Test(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]
    http_method_names = ['get']
    queryset = user.objects.all()
    serializer_class = UserSerializer

class GoogleLogin(ModelViewSet):
    permission_classes = [AllowAny]
    authentication_classes = [TokenAuthentication]

    def list(self, request, *args, **kwargs):
        access_token = self.request.query_params.get('access_token')
        r = requests.get(f'https://www.googleapis.com/oauth2/v1/userinfo?alt=json&access_token={access_token}')
        print(r.url)
        print(r.status_code)

        return Response({"data": r.json()})