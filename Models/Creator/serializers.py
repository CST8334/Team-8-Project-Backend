from rest_framework import serializers
from .models import CreatorProductRequest
from .models import CreatorReferralInvitation
from .models import CreatorCampaign
from .models import CreatorAdCard


class CreatorProductRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorProductRequest
        fields = [
            'pk',
            'creator_user_id',
            'request_type',
            'creation_time',
        ]


class CreatorReferralInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorReferralInvitation
        fields = [
            'pk',
            'inviting_creator_id',
            'invitee_creator_id',
            'invitee_creator_email',
            'creation_time'
        ]


class CreatorCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorCampaign
        fields = [
            'pk',
            'state',
            'creation_time',
            'completion_time',
            'description'
        ]


class CreatorAdCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatorAdCard
        fields = [
            'pk',
            'creator_user',
            'brand_user',
            'brand_campaign',
            'creator_campaign',
            'state',
            'price',
            'platform',
            'execution_deadline',
            'creation_time',
            'dreamwell_approval_time',
            'dreamwell_rejection_time',
            'completion_time',
            'description'
        ]
