from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Data(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.first_name
