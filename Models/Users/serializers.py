from rest_framework import serializers
from .models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
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
            'instagramName'
        ]
