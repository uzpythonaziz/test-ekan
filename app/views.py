from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category,Product
from .serializers import ProductSerializer,CategorySerializer

class AllProduct(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class AllCategory(APIView):
    def get(self,request):
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class DetailProduct(APIView):
    def get(self,request,id):
        try:
            product=Product.objects.filter(product=id)
            serializer=ProductSerializer(product,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

class DetailwithProduct(APIView):
    def get(self,request,category):
        try:
            product=Product.objects.get(category=category)
            serializer=ProductSerializer(product)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)
class DetailCategory(APIView):
    def get(self,request,id):
        try:
            category=Category.objects.get(id=id)
            serializer=CategorySerializer(category)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)