from django.db import models
from django.contrib.auth.hashers import make_password


class Users(models.Model):
    user_type = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    organization_id = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    # Claudio - new fields to include social media platform data - July 15, 2021
    googleId = models.CharField(max_length=255, null=True, blank=True)
    googleName = models.CharField(max_length=255, null=True, blank=True)
    googleEmail = models.CharField(max_length=255, null=True, blank=True)
    instagramId = models.CharField(max_length=255, null=True, blank=True)
    instagramUser = models.CharField(max_length=255, null=True, blank=True)
    instagramName = models.CharField(max_length=255, null=True, blank=True)


    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Users, self).save(*args, **kwargs)
