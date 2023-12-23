from rest_framework import viewsets
from ProjectEase_app.serializers.project import *
from ProjectEase_app.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.http import HttpResponse

# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if ((request.user.role == 'n') and (request.user.id not in project.member.all())):
            return HttpResponse("You dont have permission to delete card in this project.")
        return super().destroy(request, *args, **kwargs)


    def update(self, request, *args, **kwargs):
        project = self.get_object()
        if ((request.user.role == 'n') and not project.member.filter(id=request.user.id).exists()):
            return HttpResponse(
                "You dont have permission to update card in this project.")
        return super().update(request, *args, **kwargs)


