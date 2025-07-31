from django.db import models

from . import validators

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100, validators=[validators.must_not_int_or_float])
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title