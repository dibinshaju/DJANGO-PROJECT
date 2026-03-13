# Django Student Management Portal

A **Student Management Portal** built using **Django** that allows users to manage **Departments, Courses, and Students**.
The project demonstrates Django fundamentals such as **models, views, templates, forms, and authentication**.

---

## Features

* View list of students
* View departments
* View available courses
* Add new students using forms
* User registration system
* Django Admin panel for database management
* Template rendering with Django views
* Basic HTML layout with reusable templates

---

## Technologies Used

* Python 3
* Django
* HTML
* CSS
* SQLite (default Django database)
* Git & GitHub

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
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── migrations/
│   └── templates/
│       ├── academics/
│       │   ├── student_list.html
│       │   ├── course_list.html
│       │   ├── dept_list.html
│       │   └── student_form.html
│       └── registration/
│           └── register.html
```

---

## Database Models

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

## Installation

### 1. Clone the repository

```
git clone https://github.com/dibinshaju/DJANGO-PROJECT.git
```

### 2. Navigate to the project folder

```
cd DJANGO-PROJECT
```

### 3. Create a virtual environment

```
python -m venv env
```

### 4. Activate the virtual environment

Linux / macOS

```
source env/bin/activate
```

Windows

```
env\Scripts\activate
```

### 5. Install Django

```
pip install django
```

---

## Database Setup

Run migrations to create the database:

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

Open in browser:

```
http://127.0.0.1:8000/
```

Admin panel:

```
http://127.0.0.1:8000/admin
```

---

## Future Improvements

* Student login system
* Course enrollment feature
* Dashboard UI
* Search and filtering
* REST API with Django REST Framework
* Better frontend styling

---

## Author

Developed as a learning project using Django.
