from django.db import models

class book(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name
