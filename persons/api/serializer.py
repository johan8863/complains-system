from rest_framework import serializers
from ..models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'name',
            'last_name',
            'sex',
            'demmanded',
        )