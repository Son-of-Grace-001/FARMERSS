from django.db import models
from typing import Any
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)
    
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    

class Varieties(models.Model):
    category_var = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    weather = models.TextField()
    yields = models.TextField()
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class Disease(models.Model):
    name = models.CharField(max_length=100)
    pest_description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    varieties = models.ForeignKey(Varieties, on_delete=models.CASCADE)
    def __str__(self):
      return self.name

class Symptom(models.Model):
    disease_name = models. CharField(max_length=50)
    disease_sym = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    def __str__(self):
      return self.disease_name

class Control(models.Model):
    disease_con = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    def __str__(self):
      return self.name
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    

class ProductVarieties(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    small_description = models.CharField(max_length=200)
    description = models.TextField()
    price  = models.CharField(max_length=100)
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
      return self.name


class CropCategory(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.name
    
class CropVarieties(models.Model):
    category_var = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    weather = models.TextField()
    yields = models.TextField()
    image =models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(CropCategory, on_delete=models.CASCADE)