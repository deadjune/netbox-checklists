from django.contrib import admin
from .models import Checklist

@admin.register(Checklist)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('checklist_name')