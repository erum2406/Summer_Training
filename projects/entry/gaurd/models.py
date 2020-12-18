from django.db import models

# Create your models here.
class gaurds(models.Model):
    guser=models.CharField(max_length=100)
    gfname=models.CharField(max_length=100)
    glname=models.CharField(max_length=100)
    gpass=models.CharField(max_length=100)
    def __str__(self):
        return self.gfname