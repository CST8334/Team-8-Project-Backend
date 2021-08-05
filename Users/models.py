from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager
from django.contrib.auth.hashers import make_password


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=255, null=False, blank=False)
    organization_id = models.IntegerField(blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    user_role = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    googleId = models.CharField(max_length=255, null=True, blank=True)
    googleName = models.CharField(max_length=255, null=True, blank=True)
    googleEmail = models.CharField(max_length=255, null=True, blank=True)
    instagramId = models.CharField(max_length=255, null=True, blank=True)
    instagramUser = models.CharField(max_length=255, null=True, blank=True)
    instagramName = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserInvitation(models.Model):
    invitation_code = models.CharField(max_length=25, null=False, blank=False)
    is_used = models.BooleanField(default=False)
