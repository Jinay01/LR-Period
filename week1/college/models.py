from django.db import models

# Create your models here.


class Stream(models.Model):
    stream = models.CharField(max_length=200, null=True, default='STREAM')

    def __str__(self):
        return self.stream


class College(models.Model):
    name = models.CharField(max_length=200, null=True, default='hiii')
    stream = models.ManyToManyField(Stream)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    college = models.ForeignKey(College, null=True, on_delete=models.SET_NULL)
    stream = models.ForeignKey(Stream, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
