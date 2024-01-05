from django.urls import path
from rest_framework import routers
from .viewsets import AddressViewSet

urlpatterns = [
    
]

r = routers.DefaultRouter(trailing_slash=False)
r.register('address', AddressViewSet)
urlpatterns += r.urls