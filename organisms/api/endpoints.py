from rest_framework import generics
from .serializer import OrganismSerializer
from ..models import Organism


class OrganismList(generics.ListCreateAPIView):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer


class OrganismDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organism.objects.all()
    serializer_class = OrganismSerializer