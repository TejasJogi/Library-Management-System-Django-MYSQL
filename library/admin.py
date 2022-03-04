from django.contrib import admin
from .models import Book, IssuedBook, Student, User
from django.contrib.auth.admin import UserAdmin
from .models import User, UserType

# admin.site.unregister(Group)

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    model = Book
    search_fields = ('name','isbn', 'author', 'genere')
    list_filter = ('name','isbn', 'author', 'genere')
    ordering = ('isbn',)
    list_display = ('name','isbn', 'author', 'genere')
    fieldsets = (
        (None, {'fields': ('name','isbn', 'author', 'genere')}),
    )
    add_fieldsets = (
        (None, {'fields': ('name','isbn', 'author', 'genere')}),
    )
admin.site.register(Book, BookAdmin)


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('firstname','lastname', 'email')
    list_filter = ('firstname','lastname', 'email', 'is_staff', 'is_active')
    ordering = ('email',)
    list_display = ('firstname','lastname', 'email', 'usertype', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('firstname','lastname', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('firstname','lastname', 'email', 'password1', 'password2', 'is_active', 'is_staff')}),
    )
admin.site.register(User, UserAdminConfig) 


# class AdminConfig(admin.ModelAdmin):
#     pass                                      
# admin.site.register(Admin, AdminConfig)

class StudentAdminConfig(admin.ModelAdmin):
    model = Student
    search_fields = ('firstname','lastname', 'div','branch')
    list_filter = ( 'roll_no', 'div','branch')
    ordering = ('div',)
    list_display = ('fullname', 'roll_no', 'div','branch')
    fieldsets = (
        (None, {'fields': ('roll_no', 'div', 'branch')}),
        # ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ( 'roll_no', 'div', 'branch')}),
    )
admin.site.register(Student, StudentAdminConfig)

class IsuedBookAdmin(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook, IsuedBookAdmin)

admin.site.register(UserType)