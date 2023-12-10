from rest_framework.routers import DefaultRouter
from testing.views import Test, GoogleLogin

router = DefaultRouter()

router.register('test', Test, basename='test')
router.register('google_login', GoogleLogin, basename='google_login')

urlpatterns = router.urls
