from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.name)
