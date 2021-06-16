from dashboard.models import Influencer
from dashboard.serializers import InfluencerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class InfluencerDetails(APIView):
    """
    Retrieve an influencer instance
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk, ):
        try:
            influencer_obj = Influencer.objects.get(pk=pk)
            return influencer_obj
        except Influencer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        influencer = self.get_object(pk)
        serializer = InfluencerSerializer(influencer)
        return Response(serializer.data)


class InfluencerList(APIView):
    """
    Returns a list of all influencers stored in the database
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        influencers = Influencer.objects.all()
        influencer_serializer = InfluencerSerializer(influencers, many=True)
        return Response(influencer_serializer.data)

    def post(self, request, format=None):
        influencer_serializer = InfluencerSerializer(data=request.data)
        if influencer_serializer.is_valid():
            influencer_serializer.save()
            return Response(influencer_serializer.data, status=status.HTTP_201_CREATED)
        return Response(influencer_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
