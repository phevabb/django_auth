from django.contrib import admin
from .models import User, UserToken, Reset

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

    class Meta:
        model = User

# Register your models here.
@admin.register(UserToken)
class UserTokenAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'refresh_token', 'created_at', 'expires_at']


@admin.register(Reset)
class ResetAdmin(admin.ModelAdmin):
    list_display = ['email', 'token']