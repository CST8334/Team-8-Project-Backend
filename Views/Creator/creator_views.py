from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Creator.serializers import *
from Models.Users.serializers import *


class CreatorMarketplace(APIView):
    """
    Returns an instance of creator-ad-card
    TODO: Add "state =" as another search parameter
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_ad_card(self, creator_user_id):
        try:
            creator_ad_card = CreatorAdCard.objects.get(creator_user_id=creator_user_id)
            return creator_ad_card
        except CreatorAdCard.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        creator_ad = self.get_object(creator_user_id)
        #ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorAdCardSerializer(creator_ad)
        return Response(serializer.data)


class CreatorProfile(APIView):
    """
    Returns information about a given creator profile
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_profile(self, creator_user_id):
        try:
            creator_user = Users.objects.get(creator_user_id=creator_user_id)
            return creator_user
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        creator = self.get_objects(creator_user_id)
        serializer = UserSerializer(creator)
        return Response(serializer.data)


class NewCreator(APIView):
    """
    Saves a new creator account
    """
    permissions = [permissions.AllowAny]

    def post(self, request, format=None):
        creator_user_serializer = UserSerializer(data=request.data)
        if creator_user_serializer.is_valid():
            creator_user_serializer.save()
            return Response(creator_user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_user_serializer.errors, status.HTTP_400_BAD_REQUEST)
