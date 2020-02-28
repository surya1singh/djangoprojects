from django.contrib import admin
from . import models

class AnimalsAdmin(admin.ModelAdmin):
    list_display = ("title",  "content")
admin.site.register(models.Animals, AnimalsAdmin)
