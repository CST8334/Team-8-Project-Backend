from django.test import TestCase
from Models.Brand.models import *
from Models.Organization.models import *


class OrganizationMembershipModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(user_type="Creator", email="test@tmail.com", password="testPass", organization_id=123,
                                  user_role="user", description="test generated user", googleId='', googleName='',
                                  googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                                  tiktokEmail='')
        BrandOrganization.objects.create(description="This is a test brand organization model")
        OrganizationMembership.objects.create(user=CustomUser.objects.get(id=1),
                                              organization=BrandOrganization.objects.get(id=1),
                                              description="This is a organization membership test model")

    def test_user_label(self):
        organization_membership = OrganizationMembership.objects.get(id=1)
        field_label = organization_membership._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_organization_label(self):
        organization_membership = OrganizationMembership.objects.get(id=1)
        field_label = organization_membership._meta.get_field('organization').verbose_name
        self.assertEqual(field_label, 'organization')

    def test_description_label(self):
        organization_membership = OrganizationMembership.objects.get(id=1)
        field_label = organization_membership._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
