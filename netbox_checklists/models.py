from django.db import models

from django.contrib.contenttypes.models import ContentType

class Checklist(models.Model):
    checklist_name = models.CharField(max_length=100) #human-readable name
    related_object_types = models.ManyToManyField(
        to=ContentType
    )

    def __str__(self):
        return self.checklist_name, self.related_object_types