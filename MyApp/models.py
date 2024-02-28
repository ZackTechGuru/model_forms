from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'students'
class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.first_name

class Course(models.Model):
    course_name = models.CharField(max_length=40)
    course_lecturer = models.CharField(max_length=40)
    no_of_units = models.IntegerField()
    department = models.CharField(max_length=40)
    def __str__(self):
        return self.course_name

class Post(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=39)
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.title


# Create your models here.
