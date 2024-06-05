from rest_framework import serializers
from main.models import Products


class ProductsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 150)
    price = serializers.IntegerField()
    description = serializers.CharField(max_length = 300)

    def create(self, validated_data):
        return Products.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
