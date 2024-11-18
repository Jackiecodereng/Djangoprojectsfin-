import os

import uuid


from uuid import uuid4

from django.db import models


def generate_unique_name(instance, file_name):
    name = uuid.uuid4()
    full_file_name =f"{name}-{file_name}"
    return os.path.join("profile_pic", full_file_name)



class Customer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=generate_unique_name, null=True ) # holds the image field
    created_at = models.DateTimeField(auto_now_add=True)  # to show when it was created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}  {self.last_name} {self.gender}"  #shows in django admin f,l,g

    class Meta:
        db_table = 'customers'


class Deposit(models.Model):

    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name} - {self.amount}"


    class Meta:
        db_table = 'deposits'

#python manage.py makemigrations
        #python manage.py populate
        #python manage.py migrate
