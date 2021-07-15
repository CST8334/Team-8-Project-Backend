import datetime
from django.test import TestCase
from Models.Brand.models import *
from Models.Users.models import *
from Models.Organization.models import *


class OrganizationMembershipTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_type="Brand", email="test@tmail.com", password="testPass", organization_id=123,
                             user_role="user", description="test generated user")
        BrandOrganization.objects.create(description="This is a test brand organization model")
        OrganizationMembership.objects.create(user=Users.objects.get(id=1),
                                              organization=BrandOrganization.objects.get(id=1),
                                              description="This is a organization membership test model")

    def test_organization_membership_created(self):
        """
        Organization membership models successfully created
        """
        organization_membership = OrganizationMembership.objects.get(id=1)
        self.assertEqual(organization_membership.user, Users.objects.get(id=organization_membership.user.id))
        self.assertEqual(organization_membership.organization,
                         BrandOrganization.objects.get(id=organization_membership.organization.id))
        self.assertEqual(organization_membership.description, "This is a organization membership test model")
