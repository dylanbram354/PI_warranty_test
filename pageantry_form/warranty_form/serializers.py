from rest_framework import serializers
from .models import Warranty


class WarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Warranty
        fields = ['first_name', 'last_name', 'email', 'number_of_products']
