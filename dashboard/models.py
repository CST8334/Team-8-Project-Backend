from django.db import models


# Create your models here.
class Creator(models.Model):
    creator_name = models.CharField(max_length=255)
    creator_age = models.IntegerField()
    creator_location = models.CharField(max_length=255)
    creator_date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.creator_name


class Brand(models.Model):
    brand_company_name = models.CharField(max_length=255, blank=False, null=False)
    brand_ad_campaign_in_progress = models.BooleanField(blank=False, null=False, default=False)
    brand_ad_cards_available = models.IntegerField(default=0)
    brand_ad_cards_in_progress = models.IntegerField(default=0)
    brand_ad_cards_complete = models.IntegerField(default=0)

    def __str__(self):
        return self.brand_company_name


class CreatorYoutubeChannel(models.Model):
    creator_channel_name = models.CharField(max_length=255)
    creator_id = models.ForeignKey(Creator, on_delete=models.CASCADE)

    def __str__(self):
        return self.creator_channel_name


class AdCard(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=255)
    ad_description = models.TextField()
    ad_payout_amount = models.IntegerField()

    def __str__(self):
        return self.ad_title


class CreatorAdCard(models.Model):
    creator_id = models.ForeignKey(Creator, on_delete=models.CASCADE)
    ad_card_id = models.ForeignKey(AdCard, on_delete=models.CASCADE)

    def __str__(self):
        return self.creator_id
