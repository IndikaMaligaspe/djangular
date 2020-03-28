from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializers import ListSerializer, CardSerializer
from .models import LIst, Card

class ListViewSet(ModelViewSet):
    queryset = LIst.objects.all()
    serializer_class = ListSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = (permissions.IsAuthenticated,)