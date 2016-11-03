from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from django.contrib.auth.models import Group
from . import models


class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'email', 'timestamp')
    list_display_links = ('username', 'email',)
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = None

admin.site.register(models.User, UserAdmin)

admin.site.unregister(Group)
