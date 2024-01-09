from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from apps.users.models import UserProfile


admin.site.unregister(User)


# To create one line rows for the extra properties.
class UserProfileInLine(admin.TabularInline):
    model = UserProfile


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInLine,)
