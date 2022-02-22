from django.contrib import admin
from .models import Checklist

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('checklist_name', 'related_object_types')