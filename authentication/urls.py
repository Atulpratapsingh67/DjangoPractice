from rest_framework.routers import DefaultRouter
from .views import TokenLogin

router = DefaultRouter()

router.register('login', TokenLogin, basename='login')
urlpatterns = router.urls
