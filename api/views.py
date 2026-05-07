from django.shortcuts import render
from django.http import JsonResponse
from students .models import studentsModel
from .serializers import StudentSerializers
from rest_framework .response import Response
from rest_framework import status
from rest_framework .decorators import api_view

# Create your views here.
@api_view(['GET'])
def studentviews(request):
  if request.method=="GET":
   students=studentsModel.objects.all()
   serializer=StudentSerializers(students,many=True)
   return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def studentviews(request):
  if request.method=="GET":
    students=studentsModel.objects.all()
    serializer=StudentSerializers(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)
  elif request.method=="POST":
    serializer=StudentSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetalview(request,pk):
    try:
            students=studentsModel.objects.get(pk=pk)
    except studentsModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=="GET":
       serializer=StudentSerializers(students)
       return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=="PUT":
       serializer=StudentSerializers(students,data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response (serializer.data,status=status.HTTP_200_OK)
       else:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
       students.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)   
