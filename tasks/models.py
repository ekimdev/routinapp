import uuid

from django.db import models


class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
