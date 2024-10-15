from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinLengthValidator
import datetime

# Create your models here.
    
    
class UserManager(BaseUserManager):
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
        
    
class User(AbstractUser):
    birthday = models.DateField(blank=False, null=False)
    phone_number = models.CharField(max_length=9, unique=True, blank=False, null=False, validators=[MinLengthValidator(9)])
    email = models.EmailField(unique=True, blank=False, null=False, error_messages={
        'unique': 'User with that email already exists.',
        'blank': 'Email cannot be empty.',
        'null': 'Email cannot be empty.',
    })
    
    objects = UserManager()
    
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['birthday', 'phone_number']
       




    
    


