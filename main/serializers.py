from rest_framework import serializers
from main.models import Products


class ProductsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 150)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length = 300)

