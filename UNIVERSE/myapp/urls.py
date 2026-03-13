from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('students/', views.student_list, name='students'),
    path('courses/', views.course_list, name='course_list'),
    path('api/courses/', views.api_course_list, name='api_course_list'),
    path('departments/', views.dept_list, name='dept_list'),
    path('students/add/', views.student_create, name='student_create'),
    path('register-student', views.register_user, name='register_user'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
]