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
        serializer.save()
        return Response({'post': serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Put not allowed'})
        
        try:
            instance = Products.objects.get(pk=pk)
        except:
            return Response({'error' : 'Object does not exists'})
        
        serializer = ProductsSerializer(data = request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})