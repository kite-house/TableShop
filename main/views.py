from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Products
from django.forms import model_to_dict
# Create your views here.


class ProductsAPIView(APIView):
    def get(self, request):
        return Response({'Products': list(Products.objects.all().values())})
    
    def post(self, request):
        new_product = Products.objects.create(
            title = request.data['title'],
            price = request.data['price'],
            description = request.data['description']   
        )
        return Response({'post': model_to_dict(new_product)})