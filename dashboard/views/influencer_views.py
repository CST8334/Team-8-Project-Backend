from dashboard.models import Influencer
from dashboard.serializers import InfluencerSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class InfluencerDetails(APIView):
    """
    Retrieve an influencer instance
    """

    def get_object(self, pk, ):
        try:
            return Influencer.objects.get(pk=pk)
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

    def get(self, request, format=None):
        influencers = Influencer.objects.all()
        influencer_serializer = InfluencerSerializer(influencers, many=True)
        return Response(influencer_serializer.data)

    # TODO: add a create influencer function
