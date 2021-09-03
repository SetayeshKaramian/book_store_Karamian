from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignupForm, CustomUserChangeForm
from .models import CustomUser, Address, Profile
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    add_form = SignupForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        (("اطلاعات اکانت"), {'fields': ('email', 'password')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ('admin_image_display', 'name', 'phone')
    list_filter = ('name',)
    search_fields = ('name', 'phone')


admin.site.register(Address)
admin.site.register(Profile)
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Customer)
# admin.site.register(Staff)
# admin.site.register(Admin)
