from django.contrib import admin

from .models import Property

#register catalogs
admin.site.register(Property)
