from django.contrib import admin
from registration.models import *


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User,UserAdmin)


class ChocolateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chocolate,ChocolateAdmin)
