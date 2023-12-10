from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import *

router = DefaultRouter()

router.register('login', TokenLogin, basename='login')
urlpatterns = router.urls

urlpatterns+= [
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')
]
