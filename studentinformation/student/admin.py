from django.contrib import admin
from student.models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Course)