from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    address = models.TextField()

    class Meta:
        db_table = "register"

    def get_absolute_url(self):
        return reverse("add")    

    def __str__(self):
        return self.name    