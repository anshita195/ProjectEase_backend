from rest_framework import serializers
from ProjectEase_app.models import *
from ProjectEase_app.models.list import List
from .card import CardSerializer

class ListSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True,read_only=True)
    class Meta:
        
        model=List
        fields='__all__'