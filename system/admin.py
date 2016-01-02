from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from system.models import Info, Salary, Check, Department
from django.contrib.admin.options import ModelAdmin
# Register your models here.

class InfoInline(admin.StackedInline):
    model = Info
    can_delete = False
    verbose_name_plural = 'info'
    
class UserAdmin(UserAdmin):
    list_display = ['info','username']
    inlines = (InfoInline, )

    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Salary)
admin.site.register(Check)
admin.site.register(Department)
