from django.contrib import admin
from .models import Student
from .models import Teacher
from .models import Course
from .models import Post

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Post)
