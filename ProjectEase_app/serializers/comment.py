from rest_framework import serializers
from ProjectEase_app.models import *

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields='__all__'