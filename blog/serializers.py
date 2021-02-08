from rest_framework import serializers
from .models import WildLife


# class WildLifeSerializer(serializers.HyperlinkedModelSerializer):
class WildLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WildLife
        exclude = 'img',
