from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . serializations import StudentSerializations


from . models import Student


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api(request, pk= None):
    
    if request.method== 'GET':
        if pk is not None:
            obj= Student.objects.get(id=pk)
            serializer= StudentSerializations(obj)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        obj= Student.objects.all()
        serializer= StudentSerializations(obj, many= True)
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    elif request.method== 'POST':
        data= request.data
        serializer= StudentSerializations(data= data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method== 'PUT':
        id= request.data.get('id')
        obj= Student.objects.get(pk=id)
        serializer= StudentSerializations(obj, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_502_BAD_GATEWAY)
    
    elif request.method=='PATCH':
        
        id= request.data.get('id')
        obj= Student.objects.get(pk=id)
        serializer= StudentSerializations(obj, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_502_BAD_GATEWAY)
    
    elif request.method=='DELETE':
        id=pk
        obj= Student.objects.get(pk=id)
        obj.delete()
        return Response('DELETE HO GYA Hai Bhai')
        
    
        
        
          
            
            
        
        
        
            
        
    
            
            
            
            
        #return Response('Nahi create hua bro', status= status.HTTP_403_FORBIDDEN)
        