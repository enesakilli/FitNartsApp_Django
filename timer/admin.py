from django.contrib import admin

# Register your models here.

from .models import Timer

admin.site.register(Timer)