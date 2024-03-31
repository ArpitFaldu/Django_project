from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser,User,auth
# # Create your models here.
# class User(abstractUser):
#     user_id=models.IntegerField(primary_key=True,null=False)
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     email=models.CharField(max_length=100)
    # def __str__(self):
    #     return f"{self.user.username}"


class Device(models.Model):
    device_id=models.IntegerField(primary_key=True,null=False, max_length=100)
    name=models.CharField(max_length=100)
    price= models.FloatField(max_length=10)
    Type=models.CharField(max_length=6)
    RAM=models.CharField(max_length=6)
    Storage=models.CharField(max_length=10)
    Battery=models.CharField(max_length=10)
    FrontCamera=models.CharField(max_length=6)
    date_of_release=models.DateField(auto_now=True)
    manufacturer=models.CharField(max_length=100)
    screen_height=models.FloatField(max_length=10)
    screen_width=models.FloatField(max_length=10)
    weight=models.FloatField(max_length=10)
    frontsideimg=models.ImageField(upload_to='pics/',validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    backsideimg=models.ImageField(upload_to='pics/',validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    color=models.CharField(max_length=50)
    fingerprintSensor=models.BooleanField(default=False)
    processor=models.CharField(max_length=100)



class Review(models.Model):
    class Meta:
        unique_together = (('user_id', 'device_id'),)
    user_id = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE,max_length=100)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE,max_length=100)
    description=models.CharField(max_length=200)
    rating=models.IntegerField(max_length=100)


class Mobile(models.Model):
    Device=models.ForeignKey(Device,on_delete=models.CASCADE)
    network=models.CharField(max_length=100)
    rearCamera=models.CharField(max_length=10)
    refreshRate=models.CharField(max_length=10)
    screenType=models.CharField(max_length=100)

class Laptop(models.Model):
    Device=models.ForeignKey(Device,on_delete=models.CASCADE)
    generation=models.CharField(max_length=10)
    ssd=models.CharField(max_length=10)
    ports=models.CharField(max_length=100)
    os=models.CharField(max_length=100)
    graphicscard=models.CharField(max_length=100)


class Company(models.Model):
    class Meta:
        unique_together = (('company_id', 'device_id'),)
    company_id=models.IntegerField(primary_key=True,max_length=100)
    device_id=models.ForeignKey(Device,on_delete=models.CASCADE,max_length=100,null=False)


class CompanyInfo(models.Model):
    company_id=models.ForeignKey(Company, primary_key=True, on_delete=models.CASCADE,max_length=100)
    companyName=models.CharField(max_length=100)
    owner=models.CharField(max_length=100)
    marketValue=models.IntegerField(max_length=26)
    YearOfEstablishment=models.IntegerField(max_length=6)


class Wishlist(models.Model):
    class Meta:
        unique_together = (('user_id', 'device_id'),)
    user_id=models.ForeignKey(User, on_delete=models.CASCADE,max_length=100)
    device_id=models.ForeignKey(Device, on_delete=models.CASCADE,max_length=100)