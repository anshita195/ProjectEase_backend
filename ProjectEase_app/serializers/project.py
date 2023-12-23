from rest_framework import serializers
from ProjectEase_app.models import *
from .list import ListSerializer


class ProjectSerializer(serializers.ModelSerializer):
    lists = ListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

class ProjectOnlySerializer(serializers.ModelSerializer):
    class Meta:

        model = Project
        fields = '__all__'
