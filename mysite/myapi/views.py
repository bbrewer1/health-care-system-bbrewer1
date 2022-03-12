from django.shortcuts import render

from rest_framework import viewsets

from .serializers import HeroSerializer, VillainSerializer
from .models import Hero, Villain

# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all().order_by('alias')
    serializer_class = VillainSerializer