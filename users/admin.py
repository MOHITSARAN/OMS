from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from .models import User
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import Group

# Register your models here.

class ExtendUserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff',
                                       'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'user_permissions')}),
    )
    
    model = User
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_active')
        
    def save_model(self, request, obj, form, change):
        super(ExtendUserAdmin, self).save_model(request, obj, form, change)
        obj.created_by = request.user
        if obj.email == '':
            obj.email = None
        obj.save()
        

admin.site.register(User, ExtendUserAdmin)