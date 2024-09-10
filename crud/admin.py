from django.contrib import admin

from .models import *

class MyModelAdmin(admin.ModelAdmin):
    pass
admin.site.register(Crudprofiles,MyModelAdmin)