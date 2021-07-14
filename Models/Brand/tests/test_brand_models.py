from django.test import TestCase
from Models.Brand.models import *


class BrandCampaignTestCase(TestCase):
    def setUp(self):
        BrandCampaign.objects.create(state="active", completion_time="2022-01-29", description="This is a test brand campaign model")

    def test_brand_campaign_created(self):
        """
        Brand campaigns are successfully created
        """
        first_campaign = BrandCampaign.objects.get(description='This is a test brand campaign model')
        self.assertEqual(first_campaign.state, 'active')
        #self.assertEqual(first_campaign.completion_time, '2022-01-29')