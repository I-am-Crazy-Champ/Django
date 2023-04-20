from django.db import models

# Create your models here.

class ContactData(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    subject=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=122)
    location=models.TextField()
    desc=models.TextField()
    price=models.TextField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name=models.CharField(max_length=122)
    location=models.TextField()
    desc=models.TextField()
    link=models.TextField()
    tech=models.TextField()

    def __str__(self):
        return self.name