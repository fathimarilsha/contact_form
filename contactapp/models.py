from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self):
        return self.name 