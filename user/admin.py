from django.contrib import admin
from user.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_student',
    )

    ordering = ("first_name",)

    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'is_superuser',
                'is_staff',
                'is_active',
                'is_student',
            )}
         ),
    )


admin.site.register(User, UserAdmin)

# admin.site.register(User)