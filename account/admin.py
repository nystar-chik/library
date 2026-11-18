from django.contrib import admin
from .models import User, OTPCode

admin.site.register(OTPCode)

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = (
        'id',
        'is_staff',
        'username',
    )
    list_display_links = ['username']
    search_fields = (
        'email',
    )
    fieldsets = (
        (
            'Основная ифнормация',
            {
                'fields':(
                    'email',
                    'password',
                )
            }
        ),

        (
            'личная информация',
            {
                'fields':(
                    'first_name',
                    'last_name',
                )
            }
        ),

        (
            'права',
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                )
            }
        )
    )

    add_fieldsets = (
        (
            None,
            {
                'classes':('wide',),
                'fields':(
                    'email',
                    'password1',
                    'password2',
                ),
            },
        ),
    )