from django.db import models


class Users(models.Model):
    user_type = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    organization_id = models.IntegerField()
    creation_time = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(max_length=255, null=False, blank=False)