from rest_framework import viewsets
from ProjectEase_app.serializers import *
from ProjectEase_app.models.list import List
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from ProjectEase_app.models import Project
from django.http import HttpResponse
# Create your views here.


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        list = self.get_object()
        project=Project.objects.get(pk=list.project.id)
        if ((request.user.role=='n') and (request.user.id not in project.member.all())):
            return HttpResponse("You dont have permission to delete list in this project.")
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        list = self.get_object()
        project = Project.objects.get(pk=list.project.id)
        if ((request.user.role == 'n') and not project.member.filter(id=request.user.id).exists()):
            return HttpResponse(
                "You dont have permission to create list in this project.")
        return super().create(request, *args, **kwargs)
        

    def update(self, request, *args, **kwargs):
        list = self.get_object()
        print(list.project.id,"a")
        project = Project.objects.get(pk=list.project.id)
        print(project.member,"b")
        if ((request.user.role == 'n') and not project.member.filter(id=request.user.id).exists()):
            return HttpResponse(
                "You dont have permission to update list in this project.")
        return super().update(request, *args, **kwargs)
       



    # permission_classes_per_method = {
    #     "create": [IsAuthenticated, isAdminPermission or isProjectMember],
    #     "destroy": [IsAuthenticated, isAdminPermission or isProjectMember],
    #     "update": [IsAuthenticated, isAdminPermission or isProjectMember],
    #     "partial_update": [IsAuthenticated, isAdminPermission or isProjectMember],
    # }
