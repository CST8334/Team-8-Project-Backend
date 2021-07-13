from rest_framework import serializers
from .models import BrandCampaign
from .models import BrandOrganization
from .models import BrandAdCard


class BrandCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandCampaign
        fields = [
            'pk',
            'state',
            'creation_time',
            'completion_time',
            'description',
        ]


class BrandOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandOrganization
        fields = [
            'pk',
            'creation_time',
            'description'
        ]


class BrandAdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandAdCard
        fields = [
            'pk',
            'creator_campaign_id',
            'brand_campaign_id',
            'state',
            'price',
            'platform',
            'execution_deadline',
            'creation_time',
            'dreamwell_approval_time',
            'dreamwell_rejection_time',
            'completion_time',
            'brand_user_id',
            'creator_user_id',
            'brand_organization_id',
            'description'
        ]
