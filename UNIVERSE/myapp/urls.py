from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='course_list'),
    path('departments/', views.dept_list, name='dept_list'),
    path('students/add/', views.student_create, name='student_create'),
]