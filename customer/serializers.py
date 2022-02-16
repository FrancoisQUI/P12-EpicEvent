from rest_framework.serializers import ModelSerializer

from .models import Customer, Networks


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class NetworksSerializer(ModelSerializer):
    class Meta:
        model = Networks
        fields = '__all__'
