from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title price is_active created'.split()
        # fields = '__all__'
        # exclude = 'id price'.split()
