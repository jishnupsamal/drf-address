from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Country
from .serializers import CountrySerializer

class CountryListAPIView(ListAPIView):
    # model = Country
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

