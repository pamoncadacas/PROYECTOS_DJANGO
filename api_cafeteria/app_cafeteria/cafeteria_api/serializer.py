from rest_framework import serializers
from .models import Cafeteria

class CafateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = (
            "id",
            "clasificacion",
            "producto",
            "calorias",
            "precio",
            "image",
        )
        