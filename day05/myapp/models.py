from django.db import models

# Create your models here.
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=50)
    eadd=models.CharField(max_length=50)
    erank=models.IntegerField()
    ecoll=models.CharField(max_length=50)

    def __str__(self):
        return self.sname