from django.test import TestCase
from Models.Creator.models import *
from Users.models import CustomUser as Users

"""
Author: Nathen White
File: test_creator_models.py
Description: Unit tests of creator model fields
"""


class CreatorProductRequestModelTest(TestCase):
    """
    Tests creator product request models

    Methods
    -------
    test_creator_user_label()
    test_request_type_label()
    test_creation_time_label()
    """
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(user_type="Creator", email="test@tmail.com", password="testPass", organization_id=123,
                                  user_role="user", description="test generated user", googleId='', googleName='',
                                  googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                                  tiktokEmail='')
        CreatorProductRequest.objects.create(creator_user=Users.objects.get(id=1), request_type="test request")

    def test_creator_user_label(self):
        product_request = CreatorProductRequest.objects.get(id=1)
        field_label = product_request._meta.get_field('creator_user').verbose_name
        self.assertEqual(field_label, 'creator user')

    def test_request_type_label(self):
        product_request = CreatorProductRequest.objects.get(id=1)
        field_label = product_request._meta.get_field('request_type').verbose_name
        self.assertEqual(field_label, 'request type')

    def test_creation_time_label(self):
        product_request = CreatorProductRequest.objects.get(id=1)
        field_label = product_request._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')


class CreatorReferralInvitationModelTest(TestCase):
    """
    Tests creator referral invitation models

    Methods
    -------
    test_inviting_creator_label()
    test_invitee_creator_label()
    test_invitee_creator_email_label()
    test_creation_time_label()
    """
    @classmethod
    def setUpTestData(cls):
        Users.objects.create(user_type="CreatorA", email="testA@tmail.com", password="testAPass", organization_id=123,
                             user_role="user", description="test A generated user", googleId='', googleName='',
                             googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                             tiktokEmail='')
        Users.objects.create(user_type="CreatorB", email="testB@tmail.com", password="testBPass", organization_id=123,
                             user_role="user", description="test B generated user", googleId='', googleName='',
                             googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                             tiktokEmail='')
        CreatorReferralInvitation.objects.create(inviting_creator=Users.objects.get(id=1),
                                                 invitee_creator=Users.objects.get(id=2),
                                                 invitee_creator_email="testB@cmail.com")

    def test_inviting_creator_label(self):
        referral_invitation = CreatorReferralInvitation.objects.get(id=1)
        field_label = referral_invitation._meta.get_field('inviting_creator').verbose_name
        self.assertEqual(field_label, 'inviting creator')

    def test_invitee_creator_label(self):
        referral_invitation = CreatorReferralInvitation.objects.get(id=1)
        field_label = referral_invitation._meta.get_field('invitee_creator').verbose_name
        self.assertEqual(field_label, 'invitee creator')

    def test_invitee_creator_email_label(self):
        referral_invitation = CreatorReferralInvitation.objects.get(id=1)
        field_label = referral_invitation._meta.get_field('invitee_creator_email').verbose_name
        self.assertEqual(field_label, 'invitee creator email')

    def test_creation_time_label(self):
        referral_invitation = CreatorReferralInvitation.objects.get(id=1)
        field_label = referral_invitation._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')


class CreatorCampaignModelTest(TestCase):
    """
    Tests creator campaign models

    Methods
    -------
    test_state_label()
    test_creation_time_label()
    test_completion_time_label()
    test_description_label()
    """
    @classmethod
    def setUpTestData(cls):
        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29",
                                       description="This is a test creator campaign model")

    def test_state_label(self):
        creator_campaign = CreatorCampaign.objects.get(id=1)
        field_label = creator_campaign._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_creation_time_label(self):
        creator_campaign = CreatorCampaign.objects.get(id=1)
        field_label = creator_campaign._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_completion_time_label(self):
        creator_campaign = CreatorCampaign.objects.get(id=1)
        field_label = creator_campaign._meta.get_field('completion_time').verbose_name
        self.assertEqual(field_label, 'completion time')

    def test_description_label(self):
        creator_campaign = CreatorCampaign.objects.get(id=1)
        field_label = creator_campaign._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')


class CreatorAdCardModelTest(TestCase):
    """
    Tests creator ad card models

    Methods
    -------
    test_creator_user_label()
    test_brand_user_label()
    test_brand_campaign_label()
    test_creator_campaign_label()
    test_state_label()
    test_price_label()
    test_platform_label()
    test_execution_deadline_label()
    test_creation_time_label()
    test_dreamwell_approval_time_label()
    test_dreamwell_rejection_time_label()
    test_completion_time_label()
    test_description_label()
    """
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(user_type="CreatorA", email="testA@tmail.com", password="testAPass",
                                  organization_id=123, user_role="user", description="test A generated user",
                                  googleId='', googleName='', googleEmail='', instagramId='', instagramUser='',
                                  instagramName='', tiktokId='', tiktokEmail='')
        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29",
                                       description="This is a test creator campaign model")
        CreatorAdCard.objects.create(creator_user=Users.objects.get(id=1), brand_user=None, brand_campaign=None,
                                     creator_campaign=CreatorCampaign.objects.get(id=1), state="active",
                                     price=500, platform="youtube", execution_deadline="2022-01-29",
                                     dreamwell_approval_time=None, dreamwell_rejection_time=None,
                                     completion_time=None, description="This is a creator ad card test model")

    def test_creator_user_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('creator_user').verbose_name
        self.assertEqual(field_label, 'creator user')

    def test_brand_user_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('brand_user').verbose_name
        self.assertEqual(field_label, 'brand user')

    def test_brand_campaign_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('brand_campaign').verbose_name
        self.assertEqual(field_label, 'brand campaign')

    def test_creator_campaign_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('creator_campaign').verbose_name
        self.assertEqual(field_label, 'creator campaign')

    def test_state_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'state')

    def test_price_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_platform_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('platform').verbose_name
        self.assertEqual(field_label, 'platform')

    def test_execution_deadline_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('execution_deadline').verbose_name
        self.assertEqual(field_label, 'execution deadline')

    def test_creation_time_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('creation_time').verbose_name
        self.assertEqual(field_label, 'creation time')

    def test_dreamwell_approval_time_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('dreamwell_approval_time').verbose_name
        self.assertEqual(field_label, 'dreamwell approval time')

    def test_dreamwell_rejection_time_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('dreamwell_rejection_time').verbose_name
        self.assertEqual(field_label, 'dreamwell rejection time')

    def test_completion_time_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('completion_time').verbose_name
        self.assertEqual(field_label, 'completion time')

    def test_description_label(self):
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        field_label = creator_ad_card._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')
