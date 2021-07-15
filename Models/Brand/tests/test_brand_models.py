import datetime
import pytz
from django.test import TestCase
from Models.Brand.models import *
from Models.Users.models import *


class BrandCampaignTestCase(TestCase):
    def setUp(self):
        BrandCampaign.objects.create(state="active", completion_time="2022-01-29",
                                     description="This is a test brand campaign model")

    def test_brand_campaign_created(self):
        """
        Brand campaigns are successfully created
        """
        first_campaign = BrandCampaign.objects.get(id=1)
        self.assertEqual(first_campaign.state, 'active')
        date_check = datetime.datetime(2022, 1, 29, 0, 0, 0, 0, pytz.UTC)
        self.assertEqual(first_campaign.completion_time, date_check)
        self.assertEqual(first_campaign.description, "This is a test brand campaign model")


class BrandOrganizationTestCase(TestCase):
    def setUp(self):
        BrandOrganization.objects.create(description="This is a test brand organization model")

    def test_brand_organization_created(self):
        """
        Brand organizations are successfully created
        """
        first_organization = BrandOrganization.objects.get(id=1)
        self.assertEqual(first_organization.description, "This is a test brand organization model")


class BrandAdCardTestCase(TestCase):
    def setUp(self):
        BrandOrganization.objects.create(description="Brand organization")
        Users.objects.create(user_type="Brand", email="test@tmail.com", password="testPass", organization_id=123,
                             user_role="user", description="test generated user")
        BrandCampaign.objects.create(state="active", completion_time="2022-01-29",
                                     description="This is a test brand campaign model")
        BrandAdCard.objects.create(state="active", price=725, platform="Youtube", execution_deadline="2022-01-29",
                                   dreamwell_approval_time=None, dreamwell_rejection_time=None, completion_time=None,
                                   description="This is a test brand ad card model",
                                   brand_organization=BrandOrganization.objects.get(id=1),
                                   brand_user=Users.objects.get(id=1),
                                   creator_campaign=None, creator_user=None,
                                   brand_campaign=BrandCampaign.objects.get(id=1))

    def test_brand_ad_card_created(self):
        """
        Brand ad cards are successfully created
        """
        brand_ad_card = BrandAdCard.objects.get(id=1)
        self.assertEqual(brand_ad_card.state, "active")
        self.assertEqual(brand_ad_card.price, 725)
        self.assertEqual(brand_ad_card.platform, "Youtube")
        self.assertEqual(brand_ad_card.execution_deadline, datetime.date(2022, 1, 29))
        self.assertEqual(brand_ad_card.description, "This is a test brand ad card model")
        self.assertEqual(brand_ad_card.brand_organization,
                         BrandOrganization.objects.get(id=brand_ad_card.brand_organization.id))
        self.assertEqual(brand_ad_card.brand_user,
                         Users.objects.get(id=brand_ad_card.brand_organization.id))
        self.assertEqual(brand_ad_card.brand_campaign,
                         BrandCampaign.objects.get(id=brand_ad_card.brand_campaign.id))
