from django.contrib import admin
from Account.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(User, UserAdmin)
