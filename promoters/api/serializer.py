from rest_framework import serializers
from ..models import Promoter


class PromoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promoter
        fields = (
            'id',
            'person',
            'age',
            'school_level',
            'occupation',
            'address',
            'phone_or_place',
        )