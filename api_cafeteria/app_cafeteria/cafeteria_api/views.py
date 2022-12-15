from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Cafeteria
from .serializer import CafateriaSerializer

# Create your views here.
class CafeteriaApiView(APIView):
    def get(self,request,*args,**kwargs):
        '''
        LIst all the cafeteria items for given requeted user
        '''
        cafeteria = Cafeteria.objects
        serializer = CafateriaSerializer(cafeteria, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwags):
        '''
        Create the clafeteria wint given moto data
        '''
        data = {
            'clasificacion' : request.data.get('clasificacion'),
            'producto': request.data.get('producto'),
            'calorias' : request.data.get('calorias'),
            'precio' : request.data.get('precio'),
            'image' : request.data.get('image'),
        }
        serializer = CafateriaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CafeteriaDetailApiView(APIView):
    def get_objects(self, cafeteria_id):
        try:
            return Cafeteria.objects.get(id=cafeteria_id)
        except Cafeteria.DoesNotExist:
            return None

    def get(self, request, cafeteria_id, *args, **kwargs):
        cafeteria_instance = self.get_objects(cafeteria_id)
        if not cafeteria_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST    
            )
        serializer = CafateriaSerializer(cafeteria_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, cafeteria_id, *args, **kwargs):
        cafeteria_instance = self.get_object(cafeteria_id)
        if not cafeteria_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data ={
        
            'clasificacion' : request.data.get('clasificacion'),
            'producto': request.data.get('producto'),
            'calorias' : request.data.get('calorias'),
            'precio' : request.data.get('precio'),
            'image' : request.data.get('image'),
        }
        serializer = CafateriaSerializer(
            instance = cafeteria_instance,
            data=data,
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, cafeteria_id, *args, **kwargs):
        cafeteria_instance = self.get_objects(cafeteria_id)
        if not cafeteria_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        cafeteria_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
        
class CafeteriaClasificacionApiView(APIView):
    def get(self,request, cafeteria_clasificacion, *args,**kwargs):
       #filter: funciona para que busque mas de uno
        cafeteria = Cafeteria.objects.filter(clasificacion=cafeteria_clasificacion)
        serializer = CafateriaSerializer(cafeteria, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
