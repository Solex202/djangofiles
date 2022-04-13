from django.db import models


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")
    dateCreated = models.DateTimeField(auto_now_add=True)


def __str__(self) -> str:
    return self.title
