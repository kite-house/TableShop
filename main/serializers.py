from rest_framework import serializers
from main.models import Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("title", 'price', 'description')
