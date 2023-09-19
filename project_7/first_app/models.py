from django.db import models

# Create your models here.


class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self) -> str:
        return f"Roll : {self.roll} -> {self.name}"


class CommonInfoModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.TextField()

    class Meta:
        abstract = True


class StudentInfoModel(CommonInfoModel):
    tution_fee = models.IntegerField()
    section = models.IntegerField()


class TeacherInfoModel(CommonInfoModel):
    salary = models.IntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    designation = models.CharField(max_length=30)


class Manager(Employee):
    hiring = models.BooleanField()
    take_interview = models.BooleanField()


class Friend(models.Model):
    name = models.CharField(max_length=30)
    attendence = models.BooleanField()
    hw = models.TextField()


class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']
