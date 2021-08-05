from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from Models.Creator.models import CreatorProductRequest
from Models.Creator.models import CreatorReferralInvitation
from Models.Creator.models import CreatorCampaign
from Models.Creator.models import CreatorAdCard
from Models.Brand.models import BrandOrganization
from Models.Brand.models import BrandCampaign
from Models.Brand.models import BrandAdCard
from .models import UserInvitation
from Models.Organization.models import OrganizationMembership


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ordering = ('email',)
    list_display = ('email', 'user_type', 'organization_id', 'user_role', 'description', 'creation_time', 'googleId',
                    'googleName', 'googleEmail', 'instagramId', 'instagramUser', 'instagramName', 'is_staff',
                    'is_superuser', 'is_active')
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'user_type', 'organization_id', 'user_role', 'description', 'googleId',
                       'googleName', 'googleEmail', 'instagramId', 'instagramUser', 'instagramName')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


admin.site.register(CreatorCampaign)
admin.site.register(CreatorProductRequest)
admin.site.register(CreatorReferralInvitation)
admin.site.register(CreatorAdCard)
admin.site.register(BrandOrganization)
admin.site.register(BrandCampaign)
admin.site.register(BrandAdCard)
admin.site.register(OrganizationMembership)
admin.site.register(UserInvitation)
admin.site.register(CustomUser, CustomUserAdmin)
