from django.contrib import admin

# Register your models here.

from .models import Info, Prediction

admin.site.register(Info)
admin.site.register(Prediction)