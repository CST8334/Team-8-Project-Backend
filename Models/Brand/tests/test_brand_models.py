from django.test import TestCase
from Models.Brand.models import *

"""
Author: Nathen White
File: test_brand_models.py
Description: Unit tests of brand model fields
"""


class BrandCampaignModelTest(TestCase):
    """
    Test brand campaign models

    Methods
    -------
    test_state_label()
    test_creation_time_label()
    test_completion_time_label()
    test_description_label()
    """
    @classmethod
    def setUpTestData(cls):
        BrandCampaign.objects.create(state="active", completion_time="2022-01-29",
                                     description="This is a test brand campaign model")

    def test_state_label(self):
        first_campaign = BrandCampaign.objects.get(id=1)
        field_label = first_campaign._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_creation_time_label(self):
        first_campaign = BrandCampaign.objects.get(id=1)
        field_label = first_campaign._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_completion_time_label(self):
        first_campaign = BrandCampaign.objects.get(id=1)
        field_label = first_campaign._meta.get_field('completion_time').verbose_name
        self.assertEqual(field_label, 'completion time')

    def test_description_label(self):
        first_campaign = BrandCampaign.objects.get(id=1)
        field_label = first_campaign._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')


class BrandOrganizationModelTest(TestCase):
    """
    Test brand organization models

    Methods
    -------
    test_creation_time_label()
    test_description_label()
    """
    @classmethod
    def setUpTestData(cls):
        BrandOrganization.objects.create(description="This is a test brand organization model")

    def test_creation_time_label(self):
        first_organization = BrandOrganization.objects.get(id=1)
        field_label = first_organization._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_description_label(self):
        first_organization = BrandOrganization.objects.get(id=1)
        field_label = first_organization._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')


class BrandAdCardModelTest(TestCase):
    """
    Test brand ad card models

    Methods
    -------
    test_state_label()
    test_price_label()
    test_platform_label()
    test_execution_deadline_label()
    test_creation_time_label()
    test_dreamwell_approval_time_label()
    test_dreamwell_rejection_time_label()
    test_completion_time_label()
    test_description_label()
    test_brand_organization_label()
    test_brand_user_label()
    test_creator_campaign_label()
    test_creator_user_label()
    test_brand_campaign_label()
    """
    @classmethod
    def setUpTestData(cls):
        BrandOrganization.objects.create(description="Brand organization")
        CustomUser.objects.create(user_type="Brand", email="test@tmail.com", password="testPass", organization_id=123,
                                  user_role="user", description="test generated user", googleId='', googleName='',
                                  googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                                  tiktokEmail='')
        BrandCampaign.objects.create(state="active", completion_time="2022-01-29",
                                     description="This is a test brand campaign model")
        BrandAdCard.objects.create(state="active", price=725, platform="Youtube", execution_deadline="2022-01-29",
                                   dreamwell_approval_time=None, dreamwell_rejection_time=None, completion_time=None,
                                   description="This is a test brand ad card model",
                                   brand_organization=BrandOrganization.objects.get(id=1),
                                   brand_user=CustomUser.objects.get(id=1),
                                   creator_campaign=None, creator_user=None,
                                   brand_campaign=BrandCampaign.objects.get(id=1))

    def test_state_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_price_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_platform_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('platform').verbose_name
        self.assertEqual(field_label, 'platform')

    def test_execution_deadline_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('execution_deadline').verbose_name
        self.assertEqual(field_label, 'execution deadline')

    def test_creation_time_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_dreamwell_approval_time_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('dreamwell_approval_time').verbose_name
        self.assertEqual(field_label, 'dreamwell approval time')

    def test_dreamwell_rejection_time_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('dreamwell_rejection_time').verbose_name
        self.assertEqual(field_label, 'dreamwell rejection time')

    def test_completion_time_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('completion_time').verbose_name
        self.assertEqual(field_label, 'completion time')

    def test_description_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_brand_organization_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('brand_organization').verbose_name
        self.assertEqual(field_label, 'brand organization')

    def test_brand_user_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('brand_user').verbose_name
        self.assertEqual(field_label, 'brand user')

    def test_creator_campaign_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('creator_campaign').verbose_name
        self.assertEqual(field_label, 'creator campaign')

    def test_creator_user_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('creator_user').verbose_name
        self.assertEqual(field_label, 'creator user')

    def test_brand_campaign_label(self):
        brand_ad_card = BrandAdCard.objects.get(id=1)
        field_label = brand_ad_card._meta.get_field('brand_campaign').verbose_name
        self.assertEqual(field_label, 'brand campaign')
