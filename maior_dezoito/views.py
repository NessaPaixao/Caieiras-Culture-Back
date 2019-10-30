from django.shortcuts import render
from rest_framework import viewsets
from maior_dezoito.models import Responsavel
from maior_dezoito.serializers import ResponsavelSerializer


class ResponsavelViewSet(viewsets.ModelViewSet):
    queryset = Responsavel.objects.all()
    serializer_class = ResponsavelSerializer
