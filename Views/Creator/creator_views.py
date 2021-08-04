from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Creator.serializers import *
from Models.Users.serializers import *
from django.http import response
from django.contrib.auth.hashers import check_password
from django.core import serializers


class CreatorMarketplace(APIView):
    """
    Returns an instance of creator-ad-card
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_ad_card(self, creator_user_id):
        try:
            creator_ad_card = CreatorAdCard.objects.get(creator_user_id=creator_user_id)
            return creator_ad_card
        except CreatorAdCard.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        creator_ad = self.get_creator_ad_card(creator_user_id)
        # ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorAdCardSerializer(creator_ad)
        return Response(serializer.data)

    def post(self, request, format=None):
        creator_ad_serializer = CreatorAdCardSerializer(data=request.data)
        if creator_ad_serializer.is_valid():
            creator_ad_serializer.save()
            return Response(creator_ad_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_ad_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        creator_ad = CreatorAdCard.objects.get(pk=pk)
        creator_ad.delete()
        return response.HttpResponse()


class CreatorProductRequests(APIView):
    """
    Returns an instance of creator-product-request
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_product_request(self, creator_user_id):
        try:
            creator_product_request = CreatorProductRequest.objects.get(creator_user_id=creator_user_id)
            return creator_product_request
        except CreatorProductRequest.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        creator_product = self.get_creator_product_request(creator_user_id)
        # ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorProductRequestSerializer(creator_product)
        return Response(serializer.data)

    def post(self, request, format=None):
        creator_product_serializer = CreatorProductRequestSerializer(data=request.data)
        if creator_product_serializer.is_valid():
            creator_product_serializer.save()
            return Response(creator_product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_product_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        creator_product = CreatorProductRequest.objects.get(pk=pk)
        creator_product.delete()
        return response.HttpResponse()


class CreatorReferralInvitations(APIView):
    """
    Returns an instance of creator-referral-invitation
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_referral_invitation(self, inviting_creator_id):
        try:
            creator_referral_invitation = CreatorReferralInvitation.objects.get(inviting_creator_id=inviting_creator_id)
            return creator_referral_invitation
        except CreatorReferralInvitation.DoesNotExist:
            raise Http404

    def get(self, request, inviting_creator_id):
        creator_referral = self.get_creator_referral_invitation(inviting_creator_id)
        # ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorReferralInvitationSerializer(creator_referral)
        return Response(serializer.data)

    def post(self, request, format=None):
        creator_referral_serializer = CreatorReferralInvitationSerializer(data=request.data)
        if creator_referral_serializer.is_valid():
            creator_referral_serializer.save()
            return Response(creator_referral_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_referral_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        creator_referral = CreatorReferralInvitation.objects.get(pk=pk)
        creator_referral.delete()
        return response.HttpResponse()


class CreatorCampaigns(APIView):
    """
    Returns an instance of creator-campaign
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_referral_invitation(self, inviting_creator_id):
        try:
            creator_referral_invitation = CreatorReferralInvitation.objects.get(inviting_creator_id=inviting_creator_id)
            return creator_referral_invitation
        except CreatorReferralInvitation.DoesNotExist:
            raise Http404

    def get(self, request, inviting_creator_id):
        creator_referral = self.get_creator_referral_invitation(inviting_creator_id)
        # ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorReferralInvitationSerializer(creator_referral)
        return Response(serializer.data)

    def post(self, request, format=None):
        creator_referral_serializer = CreatorReferralInvitationSerializer(data=request.data)
        if creator_referral_serializer.is_valid():
            creator_referral_serializer.save()
            return Response(creator_referral_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_referral_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        creator_referral = CreatorReferralInvitation.objects.get(pk=pk)
        creator_referral.delete()
        return response.HttpResponse()


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
            creator_email = creator_user_serializer.validated_data['email']
            if not Users.objects.filter(email=creator_email).exists():
                creator_user_serializer.save()
                return Response(creator_user_serializer.data, status=status.HTTP_201_CREATED)
            return Response(creator_user_serializer.errors, status=status.HTTP_409_CONFLICT)
        return Response(creator_user_serializer.errors, status.HTTP_400_BAD_REQUEST)


class LoginCreator(APIView):
    """
    Checks if given email + password exist
    """
    permissions = [permissions.AllowAny]

    def post(self, request, format=None):
        creator_user_serializer = UserSerializer(data=request.data)
        if creator_user_serializer.is_valid():
            creator_email = creator_user_serializer.validated_data['email']
            # If the email exists, then compare the password
            if Users.objects.filter(email=creator_email).exists():
                login_user = Users.objects.get(email=creator_email)
                login_user_password = getattr(login_user, 'password')
                creator_password = creator_user_serializer.validated_data['password']
                if check_password(creator_password, login_user_password):
                    # If login is successful, return a token
                    content = {'email': creator_email}
                    return Response(content, status=status.HTTP_200_OK)
            return Response(creator_user_serializer.errors, status=status.HTTP_409_CONFLICT)
        return Response(creator_user_serializer.errors, status.HTTP_400_BAD_REQUEST)
