from dashboard.models import Creator
from dashboard.serializers import CreatorSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


class CreatorDetails(APIView):
    """
    Retrieve an creator instance
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk, ):
        try:
            creator_obj = Creator.objects.get(pk=pk)
            return creator_obj
        except Creator.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        creator = self.get_object(pk)
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)


class CreatorList(APIView):
    """
    Returns a list of all creators stored in the database
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        creators = Creator.objects.all()
        creator_serializer = CreatorSerializer(creators, many=True)
        return Response(creator_serializer.data)

    def post(self, request, format=None):
        creator_serializer = CreatorSerializer(data=request.data)
        if creator_serializer.is_valid():
            creator_serializer.save()
            return Response(creator_serializer.data, status=status.HTTP_201_CREATED)
        return Response(creator_serializer.erros, status=status.HTTP_400_BAD_REQUEST)
