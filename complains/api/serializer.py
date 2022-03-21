from rest_framework import serializers
from ..models import Complain


class ComplainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complain
        fields = (
            'id',
            'reception_date',
            'promoter',
            'demmanded_entity',
            'demmanded_person',
            'management_level',
            'belonging_entity',
            'problem',
        )