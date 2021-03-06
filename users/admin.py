from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'last_name', 'first_name', 'middle_name',)
    list_filter = ('email', 'last_name',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'last_name', 'first_name', 'middle_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'last_name', 'first_name', 'middle_name')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
#             'fields': ('username', 'last_name', 'first_name', 'middle_name', 'email', 'password', 'confirm_password')}

