from django.urls import path 
from .import views

urlpatterns=[
    path('students/',views.studentviews),
    path('students/<int:pk>/',views.studentDetalview)
]