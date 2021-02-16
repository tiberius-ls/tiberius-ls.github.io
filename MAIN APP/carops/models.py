from django.db import models 
from django.shortcuts import render
from django.template.defaultfilters import slugify

# Create your models here.
class Client(models.Model):
    first_name=models.CharField(max_length=50,null=True,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=50,blank=True)
    phone_number=models.CharField(max_length=50,blank=True)
    display_picture=models.ImageField(max_length=50, null=True)
    address=models.TextField(max_length=50,null=True,blank=True)
    slug = models.SlugField(blank=True, null=True)


    
    def __str__(self):
        return str(self.first_name)
    def get_detail_page(self):
        return reverse('model-name-detail',kwargs={'slug':self.slug})
        def save(self, *args, **kwargs):
            if self.name:
                self.slug = slugify(str(self.name))
                super().save(*args, **kwargs)


class Car(models.Model):
    owner=models.ForeignKey('Client', on_delete=models.CASCADE)
    car_name =models.CharField(max_length=50,null=True,blank=True)
    publish=models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return str(self.owner)
    def get_detail_page(self):
        return reverse('model-name-detail',kwargs={'slug':self.slug})
        def save(self, *args, **kwargs):
            if self.name:
                self.slug = slugify(str(self.name))
                super().save(*args, **kwargs)

    

class Contact(models.Model):
    email=models.CharField(max_length=50,null=True,blank=True)
    phone_number=models.CharField(max_length=50,null=True,blank=True)
    message=models.TextField(max_length=200,null=True)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return str(self.email)
    def get_detail_page(self):
        return reverse('model-name-detail',kwargs={'slug':self.slug})
        def save(self, *args, **kwargs):
            if self.name:
                self.slug = slugify(str(self.name))
                super().save(*args, **kwargs)


class MissingCar(models.Model):
    missing_car=models.ForeignKey('Client', on_delete=models.CASCADE)
    car_model=models.CharField(max_length=50,null=True,blank=True)
    car_plate=models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)


    def __str__(self):
        return str(self.missing_car)
    def get_detail_page(self):
        return reverse('model-name-detail',kwargs={'slug':self.slug})
        def save(self, *args, **kwargs):
            if self.name:
                self.slug = slugify(str(self.name))
                super().save(*args, **kwargs)

    

    