from rest_framework.serializers import ModelSerializer

from .models import Conversion


class ConversionSerializer(ModelSerializer):
    class Meta:
        model = Conversion
        fields = '__all__'
