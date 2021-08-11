from django.http import Http404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from Models.Organization.serializers import *


class OOMOrganizationMemberhsip(APIView):
    """
    Returns 0, 1 or many organization memberships

    Methods
    -------
    get(self, request, brand_user_id, format=None)
    """
    def get(self, request, brand_user_id, format=None):
        """
        Returns all organization memberships associated with a brand user

        Attributes
        ----------
        organization_memberships : list<OrganizationMembership>
            The organization membership objects that will be returned
        serializer : OrganizationMembershipSerializer
            Used to convert the organization membership card objects into JSON to be returned by the response
        """
        organization_memberships = OrganizationMembership.objects.all().filter(user=brand_user_id)
        serializer = OrganizationMembershipSerializer(organization_memberships, many=True)
        return Response(serializer.data)


class OrganizationMembership(APIView):
    """
    Interacts with the organization-membership table

    Methods
    -------
    get_creator_ad_card(self, creator_user_id)
    get(self, request, creator_user_id)
    post(self, request, format=None)
    delete(self, request, pk, format=None)
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_organization_membership(self, brand_user_id):
        """
        Helper method to find a creator ad card by foreign key using only the brand user's id

        Attributes
        ----------
        organization_membership : OrganizationMembership
            The organization membership found by foreign key "user"
        """
        try:
            organization_membership = OrganizationMembership.objects.get(user=brand_user_id)
            return organization_membership
        except organization_membership.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        """
        Saves or updates a organization membership

        Attributes
        ----------
        organization_membership_serializer : OrganizationMembershipSerializer
            Used to convert the JSON request body into a organization membership object
        """
        organization_membership_serializer = OrganizationMembershipSerializer(data=request.data)
        if organization_membership_serializer.is_valid():
            organization_membership_serializer.save()
            return Response(organization_membership_serializer.data, status=status.HTTP_201_CREATED)
        return Response(organization_membership_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Deletes a organization membership

        Attributes
        ----------
        organization_membership : OrganizationMembership
            The organization membership returned by primary key to be deleted
        """
        organization_membership = OrganizationMembership.objects.get(pk=pk)
        organization_membership.delete()
        return organization_membership.HttpResponse()
