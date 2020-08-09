from rest_framework import serializers
from . import models

class AcceilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Acceille
        fields = '__all__'


class FashionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fashion
        fields = '__all__'        


class GallerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Gallerie
        fields = '__all__'
        depth = 1        


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'   
        depth = 1  