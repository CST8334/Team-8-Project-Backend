from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Brand.serializers import *
from Models.Brand.models import *


class BrandAdCards(APIView):
    """
    Used to add and retrieve brand ad cards
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, format=None):
        brand_ad_serializer = BrandAdCardSerializer(data=request.data)
        if brand_ad_serializer.is_valid():
            brand_ad_serializer.save()
            return Response(brand_ad_serializer.data, status=status.HTTP_201_CREATED)
        return Response(brand_ad_serializer.errors, status.HTTP_400_BAD_REQUEST)


class BrandAdCardsList(APIView):
    """
    Returns all brand ad cards
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        brand_ad_card = BrandAdCard.objects.all()
        brand_ad_card_serializer = BrandAdCardSerializer(brand_ad_card, many=True)
        return Response(brand_ad_card_serializer.data)
