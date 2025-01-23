from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(max_length=128)  # Use hashed passwords in production

    def __str__(self):
        return self.firstname

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
   
class Event(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')]

    event_name = models.CharField(max_length=100)
    sports_name = models.CharField(max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    event_description = models.TextField()
    player_limit = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    upload_image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.event_name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    blog_date = models.DateField(auto_now_add=True)  # Automatically set to now when created
    blog_content = models.TextField(max_length=3000)
    blog_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title