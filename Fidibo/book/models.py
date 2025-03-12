from django.db import models



# Create your models here.




class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    email=models.EmailField(null=True , blank=True)
    national_id = models.CharField(max_length=11 , unique=True)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    rate = models.FloatField()
    
    
class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User,related_name="User_Comment",on_delete=models.CASCADE)
    book = models.ForeignKey(to=Book,related_name="Book_Comment",on_delete=models.CASCADE)
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    book = models.ManyToManyField(to=Book,related_name="Book_publisher")
    