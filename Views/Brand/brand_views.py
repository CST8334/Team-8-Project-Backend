from django.http import Http404
from django.http import response
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Brand.serializers import *
from Models.Brand.models import *
from Models.Users.serializers import UserSerializer

""" 
File name: brand_views.py
Created by: Nathen White
Changed by: Claudio Lima
Description: Contains all classes related to views for Brands
"""


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

class CreatorMarketplace(APIView):
    """
    Returns an instance of brand-ad-card
    TODO: Add "state =" as another search parameter
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_brand_ad_card(self, brand_user_id):
        try:
            brand_ad_card = BrandAdCard.objects.get(brand_user_id=brand_user_id, many=True)
            return brand_ad_card
        except BrandAdCard.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        brand_ad = self.get_brand_ad_card(creator_user_id)
        serializer = BrandAdCardSerializer(brand_ad)
        return Response(serializer.data)

    def post(self, request, format=None):
        brand_ad_serializer = BrandAdCardSerializer(data=request.data)
        if brand_ad_serializer.is_valid():
            brand_ad_serializer.save()
            return Response(brand_ad_serializer.data, status=status.HTTP_201_CREATED)
        return Response(brand_ad_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        brand_ad = BrandAdCard.objects.get(pk=pk)
        brand_ad.delete()
        return response.HttpResponse()

class BrandProfile(APIView):
    """
    Returns information about a given brand profile
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_brand_profile(self, brand_user_id):
        try:
            brand_user = Users.objects.get(brand_user_id=brand_user_id)
            return brand_user
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, brand_user_id):
        creator = self.get_objects(brand_user_id)
        serializer = UserSerializer(creator)
        return Response(serializer.data)


class NewBrand(APIView):
    """
    Saves a new brand account
    """
    permissions = [permissions.AllowAny]

    def post(self, request, format=None):
        brand_serializer = UserSerializer(data=request.data)
        if brand_serializer.is_valid():
            brand_email = brand_serializer.validated_data['email']
            if not Users.objects.filter(email=brand_email).exists():
                brand_serializer.save()
                return Response(brand_email.data, status=status.HTTP_201_CREATED)
            return Response(brand_email.errors, status=status.HTTP_409_CONFLICT)
        return Response(brand_serializer.errors, status.HTTP_400_BAD_REQUEST)
