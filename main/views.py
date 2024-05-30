from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Products
from .serializers import ProductsSerializer
# Create your views here.


class ProductsAPIView(APIView):
    def get(self, request):
        return Response({'Products': ProductsSerializer(Products.objects.all(), many = True).data})
    
    def post(self, request):
        serializer = ProductsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        new_product = Products.objects.create(
            title = request.data['title'],
            price = request.data['price'],
            description = request.data['description']   
        )
        return Response({'post': ProductsSerializer(new_product).data})