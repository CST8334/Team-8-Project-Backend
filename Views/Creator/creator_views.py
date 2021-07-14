from django.http import Http404
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Creator.serializers import *


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
        serializer = CreatorAdCardSerializer(creator_ad)
        return Response(serializer.data)


# class CreatorProfile(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]


