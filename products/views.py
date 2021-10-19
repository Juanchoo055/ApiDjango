# from typing import get_args
import json
import csv

from django.core.checks import messages
from django.http import request
from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.views import View



from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .serializer import ProductSerializer





from .models import Product
from products import serializer


class productView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        productos = Product.objects.all()
        serializer = ProductSerializer(productos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    
    def post (self, request):
        jd = json.loads(request.body)
        serializer = ProductSerializer(data=jd)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, safe=True)

        
class productDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request, pk):
        prod = Product.objects.get(id=pk)
        
        return JsonResponse(model_to_dict(prod))

class productUpdate(viewsets.ViewSet):

    def update(self,request,pk=None):
        prod = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=prod, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message':'success','Producto actualizado': 'si'}
        return JsonResponse(data)

    def destroy(self,request,pk=None):
        prod =Product.objects.get(id=pk)
        prod.delete()
        data = {'message':'success','Producto eliminado': 'si'}
        return JsonResponse(data)


class export(View):
    def get(self, request, *args, **kwargs):
        response =HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['name','description','price','stock'])

        for product in Product.objects.all().values_list('name','description','price','stock'):
            writer.writerow(product)
        
        response['Content-Disposition'] = (
            'attachment; filename="raport.csv"'
        )

        return response