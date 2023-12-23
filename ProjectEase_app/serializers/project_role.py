from rest_framework import serializers
from ProjectEase_app.models.project_role import *

class Project_roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_role
        fields='__all__'