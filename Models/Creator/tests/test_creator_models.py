from django.test import TestCase
from Models.Creator.models import *


class CreatorCampaignTestCase(TestCase):
    def setUp(self):
        CreatorCampaign.objects.create(state="active", completion_time="2022-01-29", description="This is a test creator campaign model")

    def test_creator_campaign_created(self):
        """
        Creator campaigns are successfully created
        """
        first_campaign = CreatorCampaign.objects.get(description='This is a test creator campaign model')
        self.assertEqual(first_campaign.state, 'active')
        #self.assertEqual(first_campaign.completion_time, '2022-01-29')
