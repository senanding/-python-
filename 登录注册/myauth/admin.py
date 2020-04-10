from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import formalVIP

# Register your models here.

class formalVIPInline(admin.TabularInline):
    model = formalVIP
    can_delete = False
    verbose_name_plural = "普通会员表"

class UserAdmin(BaseUserAdmin):
    inlines = (formalVIPInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)