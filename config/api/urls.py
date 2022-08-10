from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, DeleteAccount

app_name = 'api'


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'delete-user', DeleteAccount)
urlpatterns = [
    path('', include(router.urls)),
]

