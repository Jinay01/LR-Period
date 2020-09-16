from django.db import models

# Create your models here.


class Stream(models.Model):
    stream_name = models.CharField(max_length=200, null=True, default='STREAM')

    def __str__(self):
        return self.stream_name


class College(models.Model):
    college_name = models.CharField(max_length=200, null=True, default='hiii')
    stream_name = models.ManyToManyField(Stream)

    def __str__(self):
        return self.college_name


class Student(models.Model):
    name = models.CharField(max_length=200, null=True)
    college_name = models.ForeignKey(
        College, null=True, on_delete=models.CASCADE)
    stream_name = models.ForeignKey(
        Stream, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Committee(models.Model):
    committee_name = models.CharField(max_length=200, null=True, blank=False)
    college_name = models.ForeignKey(
        College, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.committee_name
