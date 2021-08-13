from rest_framework import serializers
from .models import OrganizationMembership

"""
Author: Nathen White
File: serializers.py
Description: Organization serializers
"""


class OrganizationMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMembership
        fields = [
            'pk',
            'user',
            'organization',
            'description',
        ]
