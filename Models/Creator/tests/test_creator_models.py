import datetime
from django.test import TestCase
from Models.Creator.models import *
from Models.Users.models import *


class CreatorCampaignTestCase(TestCase):
    def setUp(self):
        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29", description="This is a test creator campaign model")

    def test_creator_campaign_created(self):
        """
        Creator campaigns are successfully created
        """
        first_campaign = CreatorCampaign.objects.get(id=1)
        self.assertEqual(first_campaign.state, 'active')
        self.assertEqual(first_campaign.completion_time, datetime.date(2022, 1, 29))
        self.assertEqual(first_campaign.description, "This is a test creator campaign model")


class CreatorProductRequestTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_type="Creator", email="test@cmail.com", password="testPass", organization_id=321,
                             user_role="user", description="test generated user")
        CreatorProductRequest.objects.create(creator_user=Users.objects.get(id=1), request_type="test request")

    def test_creator_product_request_created(self):
        """
        Creator product request models are successfully created
        """
        product_request_test = CreatorProductRequest.objects.get(id=1)
        self.assertEqual(product_request_test.creator_user,
                         Users.objects.get(id=product_request_test.creator_user.id))
        self.assertEqual(product_request_test.request_type, "test request")


class CreatorReferralInvitationTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_type="CreatorA", email="testA@cmail.com", password="testAPass", organization_id=111,
                             user_role="user", description="test A generated user")
        Users.objects.create(user_type="CreatorB", email="testB@cmail.com", password="testBPass", organization_id=222,
                             user_role="user", description="test B generated user")
        CreatorReferralInvitation.objects.create(inviting_creator=Users.objects.get(id=1),
                                                 invitee_creator=Users.objects.get(id=2),
                                                 invitee_creator_email="testB@cmail.com")

    def test_creator_referral_invitation_created(self):
        """
        Creator referral invitation models are successfully created
        """
        creator_referral = CreatorReferralInvitation.objects.get(id=1)
        self.assertEqual(creator_referral.inviting_creator, Users.objects.get(id=creator_referral.inviting_creator.id))
        self.assertEqual(creator_referral.invitee_creator, Users.objects.get(id=creator_referral.invitee_creator.id))
        self.assertEqual(creator_referral.invitee_creator_email, "testB@cmail.com")


class CreatorAdCardTestCase(TestCase):
    def setUp(self):
        Users.objects.create(user_type="CreatorA", email="testA@cmail.com", password="testAPass", organization_id=111,
                             user_role="user", description="test A generated user")
        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29",
                                       description="This is a test creator campaign model")
        CreatorAdCard.objects.create(creator_user=Users.objects.get(id=1), brand_user=None, brand_campaign=None,
                                     creator_campaign=CreatorCampaign.objects.get(id=1), state="active",
                                     price=500, platform="youtube", execution_deadline="2022-01-29",
                                     dreamwell_approval_time=None, dreamwell_rejection_time=None,
                                     completion_time=None, description="This is a creator ad card test model")

    def test_creator_ad_card_create(self):
        """
        Creator ad card models are successfully created
        """
        creator_ad_card = CreatorAdCard.objects.get(id=1)
        self.assertEqual(creator_ad_card.creator_user, Users.objects.get(id=creator_ad_card.creator_user.id))
        self.assertEqual(creator_ad_card.creator_campaign, CreatorCampaign.objects.get(id=creator_ad_card.creator_campaign.id))
        self.assertEqual(creator_ad_card.state, "active")
        self.assertEqual(creator_ad_card.price, 500)
        self.assertEqual(creator_ad_card.platform, "youtube")
        self.assertEqual(creator_ad_card.execution_deadline, datetime.date(2022, 1, 29))
        self.assertEqual(creator_ad_card.description, "This is a creator ad card test model")
