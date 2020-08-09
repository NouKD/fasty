from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from actions.action import Actions
from . import models
# Register your models here.



class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [ProfileInline]


def _register(model, admin_class):
    admin.site.register(model, admin_class)

admin.site.unregister(User)

_register(User, UserAdmin)