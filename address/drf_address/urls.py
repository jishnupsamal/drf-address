from django.contrib import admin
from django.urls import path, include
from .routers import r

urlpatterns = [
    path('', include(r.urls)),
]