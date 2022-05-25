from django.db import models

# Create your models here.
class Address (models.Model):
    MALE = 'male'
    FEMALE = 'female'
    SEX_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(choices=SEX_CHOICES, max_length=6)
    email_Address = models.CharField(max_length=100)
    Account_number = models.CharField(max_length=100, unique=True)
    Transaction_ID = models.CharField(max_length=100, unique=True)
    Deposited_Date = models.CharField(max_length=100)
    
    
    