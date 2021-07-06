from rest_framework import serializers
from .models import Creator
from .models import Brand
from .models import CreatorYoutubeChannel
from .models import AdCard
from .models import CreatorAdCard


class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = [
            'pk',
            'creator_name',
            'creator_age',
            'creator_location',
            'creator_date_joined',
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


# TODO: add creator youtube channels to the creator serializer
class CreatorYoutubeChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorYoutubeChannel
        fields = [
            'pk',
            'creator_channel_name',
            'creator_id',
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


class CreatorAdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorAdCard
        fields = [
            'creator_id',
            'ad_card_id',
        ]
