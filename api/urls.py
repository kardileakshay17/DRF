from django.urls import path 
from .import views

urlpatterns=[
    path('students/',views.studentviews),
    path('students/<int:pk>/',views.studentDetalview),

    path('employees/',views.employeeviews.as_view()),

    path('employees/<int:pk>/',views.employeeDetails.as_view())

]