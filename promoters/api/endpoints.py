from rest_framework import generics
from .serializer import PromoterSerializer
from ..models import Promoter


class PromoterList(generics.ListCreateAPIView):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer


class PromoterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promoter.objects.all()
    serializer_class = PromoterSerializer