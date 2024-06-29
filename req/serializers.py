from rest_framework import serializers
from .models import Snipte


class SnipteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snipte
        fields = '__all__'
