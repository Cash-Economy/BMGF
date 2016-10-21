from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import MoneyUser, Pool, PoolMembership, UserContribution, UserPointMovement, UserGoal
from .forms import MoneyUserChangeForm, MoneyUserCreationForm


class MoneyUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'birth_day', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'first_name', 'last_name', 'gender', 'birth_day', 'phone_number')}
         ),
    )
    form = MoneyUserChangeForm
    add_form = MoneyUserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


class PoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'minimum_deposit', 'creation_date')


class PoolMembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'date_joined')


class UserContributionAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_name', 'txn_amount', 'balance', 'time')

    def get_name(self, obj):
        return obj.group.name

    get_name.short_description = 'Pool Name'
    get_name.admin_order_field = 'group__name'


class UserPointMovementAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'txn_amount', 'balance', 'time')


class UserGoalAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'description', 'amount')


admin.site.register(MoneyUser, MoneyUserAdmin)
admin.site.unregister(Group)

admin.site.register(Pool, PoolAdmin)
admin.site.register(PoolMembership, PoolMembershipAdmin)
admin.site.register(UserContribution, UserContributionAdmin)
admin.site.register(UserPointMovement, UserPointMovementAdmin)
admin.site.register(UserGoal, UserGoalAdmin)
