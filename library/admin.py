from django.contrib import admin
from .models import Book, NewUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('user_name', 'email')
    list_filter = ('user_name', 'email',  'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('user_name', 'email', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('user_name', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('user_name', 'email', 'password1', 'password2', 'is_active', 'is_staff')}),
    )


admin.site.register(NewUser, UserAdminConfig)