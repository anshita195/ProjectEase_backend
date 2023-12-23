from rest_framework import viewsets
from ProjectEase_app.serializers.project_role import *
from ProjectEase_app.models import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class Project_roleViewSet(viewsets.ModelViewSet):
    queryset = Project_role.objects.all()
    serializer_class = Project_roleSerializer
    permission_classes = [IsAuthenticated]
   
