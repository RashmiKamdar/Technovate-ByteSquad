# models.py

from django.db import models

"""class SourceTable(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    FullName = models.CharField(max_length=200)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=10)
    Height = models.DecimalField(max_digits=5, decimal_places=2)
    Weight = models.DecimalField(max_digits=5, decimal_places=2)
    BloodGroup = models.CharField(max_length=5)
    OrganToDonate = models.CharField(max_length=50)
    MedicalHistory = models.TextField()
    Image = models.ImageField(upload_to='source_images/')
    Living = models.BooleanField(default=True)
    Status = models.CharField(max_length=20)

    class Meta:
        db_table = 'donor'"""

class DestinationTable(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    FullName = models.CharField(max_length=200)
    Age = models.PositiveIntegerField()
    Gender = models.CharField(max_length=10)
    Height = models.DecimalField(max_digits=5, decimal_places=2)
    Weight = models.DecimalField(max_digits=5, decimal_places=2)
    BloodGroup = models.CharField(max_length=5)
    OrganToDonate = models.CharField(max_length=50)
    MedicalHistory = models.TextField()
    Image = models.ImageField(upload_to='destination_images/')
    Status = models.CharField(max_length=20)

    class Meta:
        db_table = 'deceased'
