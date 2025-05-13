import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "M3L5D.settings")

django.setup()

from M3L5DZ.models import Subject, Teacher, Grade, Student, Class, Schedule

name = input("project name")
description = input("description: ")
if Subject.objects.filter(name=name).exists():
    print("this Subject is not exit")
else:
    Subject.objects.create(name=name, description=description)
    print("Subject added")