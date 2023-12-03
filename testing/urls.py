from rest_framework.routers import DefaultRouter
from testing.views import Test

router = DefaultRouter()

router.register('test', Test, basename='test')

urlpatterns = router.urls
