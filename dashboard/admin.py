from django.contrib import admin

from Models.Creator.models import *
from Models.Brand.models import *
from Models.Users.models import *
from Models.Organization.models import *


# Register your models here.
admin.site.register(CreatorCampaign)
admin.site.register(CreatorProductRequest)
admin.site.register(CreatorReferralInvitation)
admin.site.register(CreatorAdCard)
admin.site.register(BrandOrganization)
admin.site.register(BrandCampaign)
admin.site.register(BrandAdCard)
admin.site.register(OrganizationMembership)
admin.site.register(Users)
