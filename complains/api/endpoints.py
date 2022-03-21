from rest_framework import generics
from .serializer import ComplainSerializer
from ..models import Complain


class ComplainList(generics.ListCreateAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer


class ComplainDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Complain.objects.all()
    serializer_class = ComplainSerializer