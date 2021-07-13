from django.db import models
from Models.Users.models import Users
# from django.apps import apps
# apps.get_model('Brand.')


class CreatorProductRequest(models.Model):
    creator_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='c_user_fk')  # Foreign key of users table primary key
    request_type = models.fields.CharField(max_length=255, null=False)
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.creator_user_id


class CreatorReferralInvitation(models.Model):
    inviting_creator_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='c_invite_fk')  # Foreign key from Users table
    invitee_creator_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='c_invitee_fk') # Foreign key from Users table
    invitee_creator_email = models.CharField(max_length=255, null=False, blank=False)
    creation_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.inviting_creator_id + self.invitee_creator_id


class CreatorCampaign(models.Model):
    state = models.CharField(max_length=255, null=False)
    creation_time = models.DateField(auto_now_add=True)
    completion_time = models.DateField()
    description = models.TextField()


class CreatorAdCard(models.Model):
    creator_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='c_user_id_fk') # Foreign key from users
    brand_user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='b_user_id_fk') # Foreign key from users
    brand_campaign_id = models.ForeignKey('Brand.BrandCampaign', on_delete=models.CASCADE, related_name='b_camp_id_fk') # Foreign key from BrandCampaign
    creator_campaign_id = models.ForeignKey(CreatorCampaign, on_delete=models.CASCADE, related_name='c_camp_id_fk') # Foreign key from CreatorCampaign
    state = models.CharField(max_length=255, null=False)
    price = models.FloatField()
    platform = models.CharField(max_length=255, null=False)
    execution_deadline = models.DateField()
    creation_time = models.DateField(auto_now_add=True)
    dreamwell_approval_time = models.DateField()
    dreamwell_rejection_time = models.DateField()
    completion_time = models.IntegerField(null=False)
    description = models.TextField()
