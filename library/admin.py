from django.contrib import admin
from .models import Book, User, Student
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('user_name', 'email')
    list_filter = ('user_name', 'email',  'is_admin', 'is_student')
    ordering = ('email',)
    list_display = ('user_name', 'email', 'is_admin', 'is_student')
    fieldsets = (
        (None, {'fields': ('user_name', 'email')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('user_name', 'email', 'password1', 'password2', 'is_admin', 'is_student')}),
    )
admin.site.register(User, UserAdminConfig)


class StudentAdminConfig(admin.ModelAdmin):
    # model = Student
    # search_fields = ('first_name','last_name', 'div','branch')
    # list_filter = ('first_name','last_name', 'div','branch')
    # ordering = ('div',)
    # list_display = ('first_name','last_name','roll_no', 'div', 'branch')
    # fieldsets = (
    #     (None, {'fields': ('first_name','last_name','email', 'roll_no', 'div', 'branch')}),
        
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide'),
    #         'fields': ('first_name','last_name','email', 'roll_no', 'div', 'branch')}),
    # )
    pass
admin.site.register(Student, StudentAdminConfig)