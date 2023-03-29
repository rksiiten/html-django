from django.contrib import admin

# Register your models here.

from .models import Person

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "brand")

admin.site.register(Person)