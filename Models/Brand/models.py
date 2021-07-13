from django.db import models
from Models.Creator.models import CreatorCampaign
from Models.Users.models import Users


class BrandOrganization(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class BrandCampaign(models.Model):
    state = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField()
    description = models.TextField()


class BrandAdCard(models.Model):
    creator_campaign_id = models.ForeignKey(CreatorCampaign, on_delete=models.CASCADE, related_name='c_campaign_fk') # Foreign key to CreatorCampaign
    brand_campaign_id = models.ForeignKey(BrandCampaign, on_delete=models.CASCADE, related_name='b_campaign_fk') # Foreign key to BrandCampaign
    state = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    platform = models.CharField(max_length=255, null=False)
    execution_deadline = models.DateField()
    creation_time = models.DateField(auto_now_add=True)
    dreamwell_approval_time = models.DateField()
    dreamwell_rejection_time = models.DateField()
    completion_time = models.DateField()
    brand_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, null=False, related_name='b_user_fk') # foreign key from Users
    creator_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='c_user_b_ad_fk') # foreign key from Users
    brand_organization_id = models.ForeignKey(BrandOrganization, on_delete=models.CASCADE, related_name='b_org_id') # foreign key from BrandOrganization
    description = models.TextField()
