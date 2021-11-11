from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Subscriber(models.Model):
    """
    This is Email accounts
    """
    
    email = models.EmailField(max_length=50)
    is_avtive = models.BooleanField(default=True,blank=True)

    created_at = models.DateTimeField(auto_now=True,blank=True)
    update_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=1000)
    message = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name




class Customer(models.Model):
    full_name = models.CharField(max_length=30)
    level = models.CharField(max_length=20)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.full_name



class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'blog_image')
    is_published = models.BooleanField(default = False,blank=True)

    created_at = models.DateTimeField(auto_now=True,blank=True)
    update_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title




class About(models.Model):
    # title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000,blank=True,null=True)
    about_image = models.ImageField(upload_to = 'media/about')

    def __str__(self):
        return self.title



class Team(models.Model):
    full_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'team_image')

    def __str__(self):
        return self.full_name


class Address(models.Model):
    location = models.TextField(max_length=1000,default="Nizami rayonu Əlişir Nəvai küç. 11")
    phone = models.CharField(max_length=20,default='012-574-00-04')
    email = models.EmailField(default='office@beteko.az',blank=True)

    def __str__(self):
        return self.email








