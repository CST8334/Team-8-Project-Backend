from django.db import models
from Users.models import CustomUser


class CreatorProductRequest(models.Model):
    creator_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='c_user_fk')  # Foreign key of users table primary key
    request_type = models.fields.CharField(max_length=255, null=False)
    creation_time = models.DateField(auto_now_add=True)


class CreatorReferralInvitation(models.Model):
    inviting_creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='c_invite_fk')  # Foreign key from Users table
    invitee_creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='c_invitee_fk') # Foreign key from Users table
    invitee_creator_email = models.CharField(max_length=255, null=False, blank=False)
    creation_time = models.DateField(auto_now_add=True)


class CreatorCampaign(models.Model):
    state = models.CharField(max_length=255, null=False)
    creation_time = models.DateField(auto_now_add=True)
    completion_time = models.DateField()
    description = models.TextField()


class CreatorAdCard(models.Model):
    creator_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='c_user_id_fk') # Foreign key from users
    brand_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='b_user_id_fk') # Foreign key from users
    brand_campaign = models.ForeignKey('Brand.BrandCampaign', on_delete=models.CASCADE, blank=True, null=True, related_name='b_camp_id_fk') # Foreign key from BrandCampaign
    creator_campaign = models.ForeignKey(CreatorCampaign, on_delete=models.CASCADE, related_name='c_camp_id_fk') # Foreign key from CreatorCampaign
    state = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    platform = models.CharField(max_length=255, null=False)
    execution_deadline = models.DateField()
    creation_time = models.DateField(auto_now_add=True)
    dreamwell_approval_time = models.DateField(null=True, blank=True)
    dreamwell_rejection_time = models.DateField(null=True, blank=True)
    completion_time = models.DateField(null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        return super(CreatorAdCard, self).save(*args, **kwargs)
