from django.db import models

# Create your models here.
class survey(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    def __str__(self):
        return self.name