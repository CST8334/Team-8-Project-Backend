from rest_framework import serializers
from .models import CustomUser

"""
Author: Nathen White
File: serializers.py
Description: Custom user model serializer
"""


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'pk',
            'user_type',
            'email',
            'password',
            'organization_id',
            'creation_time',
            'user_role',
            'description',
            'googleId',
            'googleName',
            'googleEmail',
            'instagramId',
            'instagramUser',
            'instagramName',
            'tiktokId',
            'tiktokEmail'
        ]
