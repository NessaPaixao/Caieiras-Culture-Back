from django.shortcuts import render
from rest_framework import viewsets
from menor_dezoito.models import Menor
from menor_dezoito.serializers import MenorSerializer


class MenorViewSet(viewsets.ModelViewSet):
    queryset = Menor.objects.all()
    serializer_class = MenorSerializer

