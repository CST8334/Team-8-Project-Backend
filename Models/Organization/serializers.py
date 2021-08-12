from rest_framework import serializers
from .models import OrganizationMembership


class OrganizationMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMembership
        fields = [
            'pk',
            'user',
            'organization',
            'description',
        ]
