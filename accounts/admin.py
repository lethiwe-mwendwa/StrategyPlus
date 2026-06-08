from django.contrib import admin
from .models import Organisation, Membership

# Register your models here.

admin.site.register(Organisation)

admin.site.register(Membership)
