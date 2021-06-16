from rest_framework import serializers
from .models import Influencer
from .models import Brand
from .models import InfluencerYoutubeChannel
from .models import AdCard
from .models import InfluencerAdCard


class InfluencerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Influencer
        fields = [
            'pk',
            'influencer_name',
            'influencer_age',
            'influencer_location',
            'influencer_date_joined',
        ]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            'pk',
            'brand_company_name',
            'brand_ad_campaign_in_progress',
            'brand_ad_cards_available',
            'brand_ad_cards_in_progress',
            'brand_ad_cards_complete',
        ]


# TODO: add influencer youtube channels to the influencer serializer
class InfluencerYoutubeChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerYoutubeChannel
        fields = [
            'pk',
            'influencer_channel_name',
            'influencer_id',
        ]


class AdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCard
        fields = [
            'pk',
            'brand_id',
            'ad_title',
            'ad_description',
            'ad_payout_amount',
        ]


class InfluencerAdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerAdCard
        fields = [
            'influencer_id',
            'ad_card_id',
        ]
