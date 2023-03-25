from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # on_delete: For one-to-many relations (CASCADE or SET_NULL)
    content = models.TextField(null=False, blank=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[:25] + "...")
