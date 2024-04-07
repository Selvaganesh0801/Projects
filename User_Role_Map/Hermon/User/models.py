from django.db import models

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=10)
    notes = models.CharField(max_length=20)
    status = models.IntegerField(default=1)

    def __str__(self):
        return self.role_name

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    phone_no = models.IntegerField(null=True,max_length=10)
    created_by = models.IntegerField(null=True)
    created_date = models.DateField()
    updated_by = models.IntegerField(null=True)
    updated_date = models.DateField()
    status = models.IntegerField(default=1)
    role_data = models.ManyToManyField(Role)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True)
    status = models.IntegerField(default=1)

    def __str__(self):
        return "User ID: " + str(self.user.id) + " -  Role ID: " + str(self.role.id)

