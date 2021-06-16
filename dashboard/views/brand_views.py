from dashboard.models import Brand
from dashboard.serializers import BrandSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class BrandDetails(APIView):
    """
    Retrieve a brand instance
    """

    def get_brand_object(self, pk):
        try:
            return Brand.objects.get(pk=pk)
        except Brand.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        brand = self.get_brand_object(pk)
        brand_serializer = BrandSerializer(brand)
        return Response(brand_serializer.data)


class BrandList(APIView):
    """
    Returns a list of all the brands stored in the database
    """

    def get(self, request, format=None):
        brands = Brand.objects.all()
        brand_serializer = BrandSerializer(brands, many=True)
        return Response(brand_serializer.data)

    # TODO: add a create brand function
