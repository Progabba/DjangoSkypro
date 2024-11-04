from django.contrib import admin

from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'phone_number', 'country')
    list_filter = ('country',)
    search_fields = ('country', 'email')


