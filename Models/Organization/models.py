from django.db import models
from Users.models import CustomUser


class OrganizationMembership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id_fk')  # foreign key from users table
    organization = models.ForeignKey('Brand.BrandOrganization',
                                        on_delete=models.CASCADE, related_name='org_id_fk')  # Foreign key from BrandOrganization table
    description = models.TextField()
