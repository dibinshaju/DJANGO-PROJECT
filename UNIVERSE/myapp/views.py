from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course, Department, Student
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentForm


def student_list(request):
    all_students = Student.objects.all()

    context = {
        'students': all_students,
        'page_title': 'Students List'
    }

    return render(request, 'academics/student_list.html', context)


def course_list(request):
    all_courses = Course.objects.all()

    context = {
        'courses': all_courses,
        'page_title': 'Available Courses'
    }

    return render(request, 'academics/course.html', context)


def dept_list(request):
    all_departments = Department.objects.all()

    context = {
        'departments': all_departments,
        'page_title': 'Available Departments'
    }

    return render(request, 'academics/dept.html', context)


def student_create(request):
    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('course_list')

    else:
        form = StudentForm()

    return render(
        request,
        'academics/student_form.html',
        {'form': form}
    )


def register_user(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )