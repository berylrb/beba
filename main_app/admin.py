from django.contrib import admin
from .models import Prompt, Car, Qualities
# Register your models here.

admin.site.register(Prompt)
admin.site.register(Car)
admin.site.register(Qualities)