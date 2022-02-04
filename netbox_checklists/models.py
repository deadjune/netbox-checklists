from django.db import models

class Checklist(models.Model):
    checklist_name = models.CharField(max_length=100) #human-readable name
    related_object_types = models.ManyToManyField(
        to=ContentType
    )
