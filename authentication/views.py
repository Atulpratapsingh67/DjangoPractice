from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from testing.serializer import UserSerializer
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

user = get_user_model()

class TokenLogin(ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    serializer_class = AuthTokenSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data.get('user')
        token, created = Token.objects.get_or_create(user=user)
        user = UserSerializer(user)
        return Response({"token": token.key,"user":user.data})
    


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client