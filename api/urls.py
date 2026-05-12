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
    path('blogs/',views.blogsViews.as_view()),
    path("comment/",views.commentViews.as_view()),

    path('blogs<int:pk/',views.blogsDetialViews.as_view()),
    path('comment<int:pk/',views.commentDetailViews.as_view())


]