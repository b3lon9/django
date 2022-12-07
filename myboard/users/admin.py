from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from users.models import Profile


# Register your models here.
'''
Profile과 User가 현재 분리되어 있기 때문에
하나도 뭉쳐서 보여주기 위함
'''
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)