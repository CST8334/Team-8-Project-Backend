from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Creator.serializers import *
from Users.serializers import UserSerializer
from Users.models import CustomUser
from Users.models import UserInvitation
from django.http import response
import uuid
from rest_framework.authtoken.models import Token


class CreatorMarketplace(APIView):
    """
    Interacts with the creator-ad-card table

    Methods
    -------
    get_creator_ad_card(self, creator_user_id)
    get(self, request, creator_user_id)
    post(self, request, format=None)
    delete(self, request, pk, format=None)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_ad_card(self, creator_user_id):
        """
        Helper method to find a creator ad card by foreign key

        Attributes
        ----------
        creator_ad_card : CreatorAdCard
            The creator ad card found by foreign key "creator_user_id"
        """
        try:
            creator_ad_card = CreatorAdCard.objects.get(creator_user_id=creator_user_id)
            return creator_ad_card
        except CreatorAdCard.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        """
        Returns a creator ad card found by foreign key

        Attributes
        ----------
        creator_id : CreatorAdCard
            The ad card object to be returned to the view
        serializer : CreatorAdCardSerializer
            Used to convert the creator ad card object in JSON to be returned by the response
        """
        creator_ad = self.get_creator_ad_card(creator_user_id)
        # Would need to set many = True in the serializer to return multiple ad cards with one call.
        # ad_cards = creator_ad.b_user_id_fk.all()
        serializer = CreatorAdCardSerializer(creator_ad)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Saves or updates a creator ad card

        Attributes
        ----------
        creator_ad_serializer : CreatorAdCardSerializer
            Used to convert the JSON request body into a creator ad card object
        """
        creator_ad_serializer = CreatorAdCardSerializer(data=request.data)
        if creator_ad_serializer.is_valid():
            creator_ad_serializer.save()
            return Response(creator_ad_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_ad_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a creator ad card

        Attributes
        ----------
        creator_ad : CreatorAdCard
            The creator ad card returned by primary key to be deleted
        """
        creator_ad = CreatorAdCard.objects.get(pk=pk)
        creator_ad.delete()
        return response.HttpResponse()


class CreatorProductRequests(APIView):
    """
    Interacts with the creator-product-request table

    Methods
    -------
    get_creator_product_request(self, creator_user_id)
    get(self, request, creator_user_id)
    post(self, request, format=None)
    delete(self, request, pk, format=None)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_product_request(self, creator_user_id):
        """
        Helper method to return a creator product request by foreign key

        Attributes
        ----------
        creator_product_request : CreatorProductRequest
            The creator product request found with given foreign key creator_user_id
        """
        try:
            creator_product_request = CreatorProductRequest.objects.get(creator_user_id=creator_user_id)
            return creator_product_request
        except CreatorProductRequest.DoesNotExist:
            raise Http404

    def get(self, request, creator_user_id):
        """
        Returns a creator product request by foreign key

        Attributes
        ----------
        creator_product : CreatorProductRequest
            The creator product object to be returned by the view
        serializer : CreatorProductRequestSerializer
            Used to serialize the data into JSON for the response
        """
        creator_product = self.get_creator_product_request(creator_user_id)
        serializer = CreatorProductRequestSerializer(creator_product)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Saves or updates a creator product request

        Attributes
        ----------
        creator_product_serializer : CreatorProductRequestSerializer
            Used to deserialize the JSON body into a creator product object
        """
        creator_product_serializer = CreatorProductRequestSerializer(data=request.data)
        if creator_product_serializer.is_valid():
            creator_product_serializer.save()
            return Response(creator_product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_product_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a creator product request

        Attributes
        ----------
        creator_product : CreatorProductRequest
            The creator product to be deleted
        """
        creator_product = CreatorProductRequest.objects.get(pk=pk)
        creator_product.delete()
        return response.HttpResponse()


class CreatorReferralInvitations(APIView):
    """
    Interacts with the creator-referral-invitation table

    Methods
    -------
    get_creator_referral_invitation(self, inviting_creator_id)
    get(self, request, inviting_creator_id)
    post(self, request, format=None)
    delete(self, request, pk, format=None)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_referral_invitation(self, inviting_creator_id):
        """
        Helper method to return a creator referral invitation model object

        Attributes
        ----------
        creator_referral_invitation : CreatorReferralInvitation
            The creator referral invitation object found by given foreign key "inviting_creator_id"
        """
        try:
            creator_referral_invitation = CreatorReferralInvitation.objects.get(inviting_creator_id=inviting_creator_id)
            return creator_referral_invitation
        except CreatorReferralInvitation.DoesNotExist:
            raise Http404

    def get(self, request, inviting_creator_id):
        """
        Returns a creator referral invitation object

        Attributes
        ----------
        creator_referral : CreatorReferralInvitation
            The creator referral object found with the helper method
        serializer : CreatorReferralInvitationSerializer
            The serializer to convert the object into JSON
        """
        creator_referral = self.get_creator_referral_invitation(inviting_creator_id)
        serializer = CreatorReferralInvitationSerializer(creator_referral)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Saves or updates a creator referral invitation

        Attributes
        ----------
        creator_referral_serializer : CreatorReferralInvitationSerializer
            The serializer deserializing the JSON request to a creator referral object
        """
        creator_referral_serializer = CreatorReferralInvitationSerializer(data=request.data)
        if creator_referral_serializer.is_valid():
            creator_referral_serializer.save()
            return Response(creator_referral_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_referral_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a creator referral invitation object based on a given primary key

        Attributes
        ----------
        creator_referral : CreatorReferralInvitation
            The creator referral invitation object to be deleted
        """
        creator_referral = CreatorReferralInvitation.objects.get(pk=pk)
        creator_referral.delete()
        return response.HttpResponse()


class CreatorCampaigns(APIView):
    """
    Interacts with the creator-campaign table

    Methods
    -------
    get_creator_campaign(self, pk)
    get(self, request, pk)
    post(self, request, format=None)
    delete(self, request, pk, format=None
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_campaign(self, pk):
        """
        Helper method to find a creator campaign object by primary key

        Attributes
        ----------
        creator_campaign : CreatorCampaign
            The creator campaign object if it exists
        """
        try:
            creator_campaign = CreatorCampaign.objects.get(pk=pk)
            return creator_campaign
        except CreatorCampaign.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        """
        Returns a creator campaign serialized object by primary key

        Attributes
        ----------
        creator_campaign : CreatorCampaign
            The creator campaign object found by primary key to be returned by the view
        serializer : CreatorCampaignSerializer
            The serializer to convert the creator campaign object into a JSON body
        """
        creator_campaign = self.get_creator_campaign(pk)
        serializer = CreatorCampaignSerializer(creator_campaign)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Saves or update a creator campaign

        Attributes
        ----------
        creator_campaign_serializer : CreatorCampaignSerializer
            The serializer deserializing a creator campaign object from the JSON request body
        """
        creator_campaign_serializer = CreatorCampaignSerializer(data=request.data)
        if creator_campaign_serializer.is_valid():
            creator_campaign_serializer.save()
            return Response(creator_campaign_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_campaign_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a creator campaign based on a given primary key

        Attributes
        ----------
        creator_campaign : CreatorCampaign
            The creator campaign to be deleted found by primary key
        """
        creator_campaign = CreatorCampaign.objects.get(pk=pk)
        creator_campaign.delete()
        return response.HttpResponse()


class CreatorProfile(APIView):
    """
    Returns information about a given creator profile

    Methods
    -------
    get_creator_profiles(self, creator_user_id)
    get(self, request, pk)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_creator_profile(self, creator_user_id):
        """
        Returns a creator profile object, found using a given primary key

        Attributes
        ----------
        creator_user : CustomUser
            The user profile model object
        """
        try:
            creator_user = CustomUser.objects.get(pk=creator_user_id)
            return creator_user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        creator = self.get_creator_profile(pk)
        serializer = UserSerializer(creator)
        return Response(serializer.data)


class CreateInvitationCode(APIView):
    """
    Adds a new invitation code to the user-invitations table and returns the code

    Methods
    -------
    get(self, request)
    """
    # Turned off for testing/demo purposes. Makes this endpoint method only usable by admin accounts.
    #permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        """
        Creates and then returns a new invitation code

        Attributes
        ----------
        invitation_code : str
            The newly generated invitation code
        new_code : UserInvitation
            The model object of the new code
        content : dict
            The JSON response holding the invitation code
        """
        invitation_code = CustomUser.objects.generate_new_invite_code()
        new_code = UserInvitation(invitation_code=invitation_code)
        new_code.save()
        content = {'invitation_code': invitation_code}
        return Response(content, status=status.HTTP_200_OK)


class NewCreator(APIView):
    """
    Saves a new creator account during signup

    Methods
    -------
    post(self, request, invitation_code, format=None)
    """
    permissions = [permissions.AllowAny]

    def post(self, request, invitation_code, format=None):
        """
        Saves a new user as part of the signup process

        Attributes
        ----------
        creator_user_serializer : serializer
            Used to deserialized the json body of the request
        invitation : str
            The invitation code object
        invalid_invitation : dict
            Error message if the invite code has already been used
        creator_email : str
            Given user email
        creator_pass : str
            Given user password
        account : account
            The new user account object
        token : Token
            The authentication token now associated with the new account
        content : dict
            The JSON body to be returned in the response
        invalid_email : dict
            Error message for if the email is already in use
        """
        creator_user_serializer = UserSerializer(data=request.data)
        if creator_user_serializer.is_valid():
            invitation = UserInvitation.objects.get(invitation_code=invitation_code)
            if getattr(invitation, 'is_used'):
                invalid_invitation = {'error_message': 'invitation code has already been used'}
                return Response(invalid_invitation, status=status.HTTP_409_CONFLICT)
            # add any other additional fields that are required to be stored on an account when a user first signs up. Ex: an organization id, instagram, google, tiktok account names etc.
            creator_email = creator_user_serializer.validated_data['email']
            creator_pass = creator_user_serializer.validated_data['password']
            if not CustomUser.objects.filter(email=creator_email).exists():
                account = CustomUser.objects.create_user(email=creator_email, password=creator_pass)
                token = Token.objects.get(user=account).key
                content = {'email': creator_email, 'token': token}
                invitation.is_used = True
                invitation.save()
                return Response(content, status=status.HTTP_201_CREATED)
            invalid_email = {'error_message': 'This email is already registered'}
            return Response(invalid_email, status=status.HTTP_409_CONFLICT)
        return Response(creator_user_serializer.errors, status.HTTP_400_BAD_REQUEST)
