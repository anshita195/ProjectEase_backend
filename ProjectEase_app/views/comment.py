from rest_framework import viewsets
from ProjectEase_app.serializers import *
from ProjectEase_app.models import *
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
