from django.contrib import admin
from registration.models import *


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)

