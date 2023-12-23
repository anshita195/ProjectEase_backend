from rest_framework import serializers
from ProjectEase_app.models import *

class Project_roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_role
        fields='__all__'