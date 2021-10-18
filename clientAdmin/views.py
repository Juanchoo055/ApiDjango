# from typing import get_args
import json

from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from .models import client



# Create your views here.
class clientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self, request):
        clients = list(client.objects.all().values())
        if len(clients)>0:
            data = {'message':'success', 'clients':clients}
        else:
            data = {'message': 'Clients not found'}

        return JsonResponse(data, safe=False)

    def post(self,request):
        print(request.body)
        jd = json.loads(request.body)
        client.objects.create(document=jd['document'],
                                first_name=jd['first_name'],
                                last_name=jd['last_name'],
                                email=jd['email'],
                                phone_number=jd['phone_number'])
        data = {'message':'success', 'clients':jd}
        return JsonResponse(data)


class clientDetailView(View):
    def get (self, request, pk):
        cliente = client.objects.get(pk=pk)
        
        return JsonResponse(model_to_dict(cliente))

    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    # def get(self,request,id=0):

    #     if id > 0:
    #         clients= list(client.objects.filter(id=id).values())
    #         if len(clients)>0:
    #             person = clients[0]
    #             datos={'messaje':"Success", 'client':person}
    #         else:
    #             datos={'messaje':"Cliente no encontrado"}
    #         return JsonResponse(datos)
    #     else:
    #         clients= list(client.objects.values())
    #         if len(clients)>0:
    #             datos={'messaje':"Success", 'clients':clients}
    #         else:
    #             datos={'messaje':"clients no encontrados"}
    #         return JsonResponse(datos)
    
    # def put(self,request,id):
    #     jd = json.loads(request.body)
    #     clients= list(client.objects.filter(id=id).values())
    #     if len(clients)>0:
    #         person=client.objects.get(id=id)
    #         person.document = jd['document'],
    #         person.first_name = jd['first_name'],
    #         person.last_name = jd['last_name'],
    #         person.email = jd['email'],
    #         person.phone_number = jd['phone_number'],
    #         person.save()
    #         datos = {'message': 'Succes'}
    #     else:
    #         datos={'messaje':"Cliente no creado"}
    #     return JsonResponse(datos)


# class clientsviewadd(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

#     def post(self,request):
#         jd = json.loads(request.body)
#         client.objects.create(document = jd['document'],
#                                 first_name = jd['first_name'],
#                                 last_name = jd['last_name'],
#                                 email = jd['email'],
#                                 phone_number = jd['phone_number'],)
#         datos = {'message': 'Succes'}
#         return JsonResponse(datos)