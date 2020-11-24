from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Customer, Company


admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Company)
