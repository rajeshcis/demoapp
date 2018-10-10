"""Student app models."""
from django.db import models
from django.utils import timezone


class Student(models.Model):
    """A Student model."""

    first_name = models.CharField(max_length=100, verbose_name='title')
    last_name = models.TextField(verbose_name='Description')
    standard = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Return string name."""
        return self.name
