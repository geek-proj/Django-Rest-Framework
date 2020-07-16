from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import UserRegistrationView

router = routers.DefaultRouter()
router.register(r'users', UserRegistrationView,basename='register')
# router.register(r'groups', views.GroupViewSet)
urlpatterns = router.urls
