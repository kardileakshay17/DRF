from django.shortcuts import render
from django.http import JsonResponse
from students .models import studentsModel
from .serializers import StudentSerializers,employeeSerializers
from rest_framework .response import Response
from rest_framework import status
from rest_framework .decorators import api_view

from rest_framework .views import APIView
from employees .models import employeeModel
from django.http import Http404

from rest_framework import mixins,generics
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

#this a start a class base views use 


# class employeeviews(APIView):
#    def get(self,request):
#       employees=employeeModel.objects.all()
#       serializer=employeeSerializers(employees,many=True)
#       return Response(serializer.data,status=status.HTTP_200_OK)
   
#    def post(self ,request):
#       serializer=employeeSerializers(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data,status=status.HTTP_201_CREATED)
#       return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
      
# class employeeDetails(APIView):
#    def get_object(self,pk):
#       try:
#          return employeeModel.objects.get(pk=pk)
#       except employeeModel.DoesNotExist:
#          raise Http404
         
#    def get(self,request,pk):
#          employee=self.get_object(pk)
#          serializer=employeeSerializers(employee)
#          return Response(serializer.data, status=status.HTTP_200_OK)
      
#    def put(self,request,pk):
#          employee=self.get_object(pk)
#          serializer=employeeSerializers(employee,data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#          return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)
   
#    def delete(self,request,pk):
#       employee=self.get_object(pk)
#       employee.delete()
#       return Response(status=status.HTTP_204_NO_CONTENT)

#mixins

class employeeviews(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
   queryset=employeeModel.objects.all()
   serializer_class=employeeSerializers
    
   def get (self,request):
      return self.list(request)
   
   def post (self,request):
      return self.create(request)
   
class employeeDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
   queryset=employeeModel.objects.all()
   serializer_class=employeeSerializers

   def get(self,request,pk):
      return self.retrieve(request)
   
   def put(self,request,pk):
      return self.update(request)
   
   def delete(self, request, pk):
       return self.destroy(request, pk)