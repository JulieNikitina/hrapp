from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'last_name', 'first_name', 'middle_name', 'email')
    list_filter = ('last_name',)
