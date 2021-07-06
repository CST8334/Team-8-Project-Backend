from dashboard.models import AdCard
from dashboard.serializers import AdCardSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class AdCardDetails(APIView):
    """
    Retrieve an Ad Card instance
    """

    def get_object(self, pk, ):
        try:
            return AdCard.objects.get(pk=pk)
        except AdCard.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        ad_card = self.get_object(pk)
        ad_card_serializer = AdCardSerializer(ad_card)
        return Response(ad_card_serializer.data)


class AdCardList(APIView):
    """
    Returns a list of all Ad Cards stored in the database
    """

    def get(self, request, format=None):
        ad_card = AdCard.objects.all()
        ad_card_serializer = AdCardSerializer(ad_card, many=True)
        return Response(ad_card_serializer.data)

    # TODO: add a create creator function
