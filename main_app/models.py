import os
import uuid

from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models her

def generate_unique_name(instance, filename):
    name = uuid.uuid4()  # universally unique id
    ext = filename.split('.')[-1]
    full_filename = f'{name}.{ext}'  # formating the files
    # full_filename='%s.%s' %(name,ext)
    return os.path.join("students", full_filename)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    other_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    id_number = models.CharField(max_length=50, unique=True, help_text="Enter your ID number")

    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20, null=True)
    dob = models.DateTimeField()
    town = models.CharField(max_length=100, null=True)
    kra_pin = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True)
    id_photo_front = models.ImageField(null=True, default="students/student.png")
    id_photo_back = models.ImageField(null=True, default="students/student.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
    return f"{self.first_name}  {self.last_name} "






