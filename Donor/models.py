from django.db import models

class UserProfile(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ])
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_group = models.CharField(max_length=5, choices=[
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        # Add other blood group options here
    ])
    organ = models.CharField(max_length=100, choices=[
        ('Heart', 'Heart'),
        ('Lungs', 'Lungs'),
        ('Liver', 'Liver'),
        # Add other organ options here
    ])
    status = models.IntegerField(choices=[
        (0, 'Living'),
        (1, 'Deceased'),
    ])
    health_history = models.TextField()
    pincode = models.CharField(max_length=10)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)

    class Meta:
        db_table = 'data'

    def __str__(self):
        return self.fullname

class UserModel(models.Model):
    """Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)"""
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
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
        db_table = 'donor'
