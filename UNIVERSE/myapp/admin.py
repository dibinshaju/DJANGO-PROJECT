from django.contrib import admin
from .models import Department, Course, Student

#basic registeration
admin.site.register(Department)

#advance registeration to customise grid
#created class to define how data looks

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits', 'semester') #colums
    list_filter = ('department', 'semester') # sidebar filters
    search_fields = ('name', 'code') # serach at top

@admin.register(Student)
class Studentadmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'enrollment_date')
    search_fields = ('first_name', 'email')