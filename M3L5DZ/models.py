from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return F'SUBJECT NAME: {self.name}'

class Teacher(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return F'TEACHER NAME: {self.name}'

class Class(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField(default=1)
    def __str__(self):
        return F'CLASS NAME: {self.name}'

class Student(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    def __str__(self):
        return F'STUDENTS NAME: {self.name}'

class Grade(models.Model):
    grade = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    data = models.CharField()

class Schedule(models.Model):
    day = models.IntegerField()
    number = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)