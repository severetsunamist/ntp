from django.contrib import admin
from .models import Property, Block, Company, CompanyCard

# main tables
admin.site.register(Property)
admin.site.register(Block)
admin.site.register(Company)
admin.site.register(CompanyCard)

