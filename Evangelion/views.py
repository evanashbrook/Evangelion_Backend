from django.shortcuts import render
from .serializers import AppSerializer
from rest_framework import generics
from .models import App


class AppListCreate(generics.ListCreateAPIView):
    serializer_class = AppSerializer
    queryset = App.objects.all()
