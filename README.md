# Student Management Portal (Django)

A simple **Student Management Portal** built using **Django**.
This project manages **Departments, Courses, and Students** and allows users to view and create student records through a web interface.

---

## Features

* View list of students
* View available courses
* View departments
* Create new student records
* User registration system
* Django admin panel for managing data
* HTML templates with base layout

---

## Technologies Used

* Python
* Django
* HTML
* CSS
* SQLite (default Django database)

---

## Project Structure

```
UNIVERSE/
│
├── manage.py
├── db.sqlite3
│
├── UNIVERSE/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
│   ├── migrations/
│   └── templates/
│       └── academics/
│           ├── student_list.html
│           ├── course_list.html
│           ├── dept_list.html
│           └── student_form.html
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/student-portal.git
```

2. Navigate to project directory

```
cd student-portal
```

3. Create virtual environment

```
python -m venv env
```

4. Activate environment

Linux / macOS

```
source env/bin/activate
```

Windows

```
env\Scripts\activate
```

5. Install dependencies

```
pip install django
```

---

## Database Setup

Run migrations to create database tables.

```
python manage.py makemigrations
python manage.py migrate
```

---

## Create Admin User

```
python manage.py createsuperuser
```

---

## Run the Server

```
python manage.py runserver
```

Open the project in your browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## Models

### Department

* name
* head_of_department
* description

### Course

* department (ForeignKey)
* name
* code
* semester
* credits

### Student

* first_name
* last_name
* email
* enrollment_date
* courses (ManyToMany)

---

## Future Improvements

* Student login system
* Course enrollment feature
* Dashboard UI
* Search and filtering
* REST API with Django REST Framework

---

## Author

Student Portal Project built for learning Django.
