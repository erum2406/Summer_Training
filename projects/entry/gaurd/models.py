from django.db import models

# Create your models here.
class gaurds(models.Model):
    guser=models.CharField(max_length=100)
    gfname=models.CharField(max_length=100)
    glname=models.CharField(max_length=100)
    gpass=models.CharField(max_length=100)
    def __str__(self):
        return self.gfname
        
class guest_entries(models.Model):
    guest_name=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    intime=models.CharField(max_length=100)
    extime=models.CharField(max_length=100)
    def __str__(self):
        return self.guest_name