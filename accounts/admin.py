from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.form import CustomUserchangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserchangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets +(
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
