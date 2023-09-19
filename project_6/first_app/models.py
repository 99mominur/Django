from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    address = models.TextField(max_length=40)
    fathers_name = models.CharField(max_length=30, default="Abdullah")
    
    def __str__(self) -> str:
        return f"Roll: {self.roll} - {self.name}"
    