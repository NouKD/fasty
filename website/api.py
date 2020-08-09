from . import models
from rest_framework import viewsets
from . import serializers
from . import models


class AcceilleViewSet (viewsets.ModelViewSet):
    queryset = models.Acceille.objects.filter(status=True)
    serializer_class = serializers.AcceilleSerializer


class FashionViewSet (viewsets.ModelViewSet):
    queryset = models.Fashion.objects.filter(status=True)
    serializer_class = serializers.FashionSerializer


class GallerieViewSet (viewsets.ModelViewSet):
    queryset = models.Gallerie.objects.filter(status=True)
    serializer_class = serializers.GallerieSerializer


class ContactViewSet (viewsets.ModelViewSet):
    queryset = models.Contact.objects.filter(status=True)
    serializer_class = serializers.ContactSerializer