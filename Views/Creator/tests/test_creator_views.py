from django.test import TestCase
from django.urls import reverse

from Models.Creator.models import CreatorCampaign, CreatorAdCard
from Users.models import CustomUser

"""
Author: Nathen White
File: test_creator_view.py
Description: Ensure viewpoints that manipulate creator models works as expected
"""


class CreatorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(user_type="CreatorA", email="testA@tmail.com", password="testAPass",
                                  organization_id=123,
                                  user_role="user", description="test A generated user", googleId='', googleName='',
                                  googleEmail='', instagramId='', instagramUser='', instagramName='', tiktokId='',
                                  tiktokEmail='')

        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29",
                                       description="This is a test creator campaign model")

        ad_cards = 5

        for ad_card_id in range(ad_cards):
            CreatorAdCard.objects.create(
                creator_user=CustomUser.objects.get(id=1),
                brand_user=None, brand_campaign=None,
                creator_campaign=CreatorCampaign.objects.get(id=1),
                state="active",
                price=500,
                platform="youtube",
                execution_deadline="2022-01-29",
                dreamwell_approval_time=None,
                dreamwell_rejection_time=None,
                completion_time=None,
                description=f'This is number {ad_card_id} creator ad card test model'
            )

    def test_ad_cards_by_creator_view(self):
        response = self.client.get('/creator-ad-card/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

    def test_bad_ad_cards_by_creator_view(self):
        response = self.client.get('/creator-ad-card/2/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(len(response.data), 5)
