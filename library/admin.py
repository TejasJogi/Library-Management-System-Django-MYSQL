from django.contrib import admin
from .models import Book, IssuedBook, Student, User
from django.contrib.auth.admin import UserAdmin
from .models import User

# admin.site.unregister(Group)

# Register your models here.

@admin.register(Book)
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

@admin.register(User)
class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('email',)
    list_display = ('username', 'first_name','last_name', 'email', 'last_login', 'is_active', 'is_staff')
    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('first_name','last_name', 'email', 'last_login')}),
        ('Permissions', {'fields': ('is_active', 'is_staff','is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('first_name','last_name', 'email', 'password1', 'password2', 'is_active', 'is_staff')}),
    )


# class AdminConfig(admin.ModelAdmin):
#     pass                                      
# admin.site.register(Admin, AdminConfig)


@admin.register(Student)
class StudentAdminConfig(admin.ModelAdmin):
    model = Student

    search_fields = ('div','branch')
    list_filter = ('roll_no', 'div','branch')
    ordering = ('div',)
    list_display = ('fullname', 'roll_no', 'div','branch')
    fieldsets = (
        (None, {'fields': ('roll_no', 'div', 'branch')}),
        
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ( 'roll_no', 'div', 'branch')}),
    )

@admin.register(IssuedBook)
class IsuedBookAdmin(admin.ModelAdmin):
    pass