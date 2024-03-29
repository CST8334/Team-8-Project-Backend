from django.db import models
from Models.Creator.models import CreatorCampaign
from Users.models import CustomUser

"""
Author: Nathen White
File: models.py
Description: Brand models
"""


class BrandOrganization(models.Model):
    creation_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class BrandCampaign(models.Model):
    state = models.CharField(max_length=255)
    creation_time = models.DateTimeField(auto_now_add=True)
    completion_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField()


class BrandAdCard(models.Model):
    state = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    platform = models.CharField(max_length=255, null=False)
    execution_deadline = models.DateField()
    creation_time = models.DateField(auto_now_add=True)
    dreamwell_approval_time = models.DateField(null=True, blank=True)
    dreamwell_rejection_time = models.DateField(null=True, blank=True)
    completion_time = models.DateField(null=True, blank=True)
    description = models.TextField()
    brand_organization = models.ForeignKey(BrandOrganization, on_delete=models.DO_NOTHING,
                                           related_name='b_org_id')  # foreign key from BrandOrganization
    brand_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, related_name='b_user_fk') # foreign key from Users
    creator_campaign = models.ForeignKey(CreatorCampaign, on_delete=models.CASCADE, blank=True, null=True,
                                         related_name='c_campaign_fk')  # Foreign key to CreatorCampaign
    creator_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='c_user_b_ad_fk') # foreign key from Users
    brand_campaign = models.ForeignKey(BrandCampaign, on_delete=models.CASCADE,
                                       related_name='b_campaign_fk')  # Foreign key to BrandCampaign

    def save(self, *args, **kwargs):
        return super(BrandAdCard, self).save(*args, **kwargs)

