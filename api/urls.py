from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.employeeviewSet, basename='employeedirectories')
urlpatterns=[
    path('students/',views.studentviews),
    path('students/<int:pk>/',views.studentDetalview),

    # path('employees/',views.employeeviews.as_view()),
    # path('employees/<int:pk>/',views.employeeDetails.as_view()),

    path('', include(router.urls)),


]