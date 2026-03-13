from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Course, Department, Student
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def student_list(request):
    all_students = Student.objects.all()

    context = {
        'students': all_students,
        'page_title': 'Students List'
    }

    return render(request, 'academics/student_list.html', context)


@login_required
def course_list(request):
    all_courses = Course.objects.all()

    context = {
        'courses': all_courses,
        'page_title': 'Available Courses'
    }

    return render(request, 'academics/course.html', context)


@login_required
def api_course_list(request):
    courses = (
        Course.objects.select_related('department')
        .all()
        .order_by('code')
    )

    data = [
        {
            "id": c.id,
            "code": c.code,
            "name": c.name,
            "semester": c.semester,
            "credits": c.credits,
            "department": {
                "id": c.department_id,
                "name": c.department.name if c.department_id else None,
            },
        }
        for c in courses
    ]

    return JsonResponse({"results": data})


@login_required
def dept_list(request):
    all_departments = Department.objects.all()

    context = {
        'departments': all_departments,
        'page_title': 'Available Departments'
    }

    return render(request, 'academics/dept.html', context)


@login_required
def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():

           
            username = request.POST.get("username", "").strip()
            password = request.POST.get("password", "").strip()
            email = request.POST.get("email", "").strip()

           
            if not username or not password or not email:
                return render(request, "academics/student_form.html", {
                    "form": form,
                    "error": "All login fields required"
                })

          
            if User.objects.filter(username=username).exists():
                return render(request, "academics/student_form.html", {
                    "form": form,
                    "error": "Username already exists"
                })

            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )

            student = form.save(commit=False)
            student.user = user
            student.save()

            form.save_m2m()

            return redirect("course_list")

    else:
        form = StudentForm()

    return render(request, "academics/student_form.html", {"form": form})


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

