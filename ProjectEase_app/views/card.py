from rest_framework import viewsets
from ProjectEase_app.serializers.card import *
from ProjectEase_app.models.card import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from ProjectEase_app.models import Project,List
from django.http import HttpResponse

# Create your views here.


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        card = self.get_object()
        list = List.objects.get(pk=card.list.id)
        project = Project.objects.get(pk=list.project.id)
        if ((request.user.role == 'n') and (request.user.id not in project.member.all())):
            return HttpResponse("You dont have permission to delete card in this project.")
        return super().destroy(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        card = self.get_object()
        list = List.objects.get(pk=card.list.id)
        project = Project.objects.get(pk=list.project.id)
        if ((request.user.role == 'n') and not project.member.filter(id=request.user.id).exists()):
            return HttpResponse(
                "You dont have permission to create card in this project.")
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        card = self.get_object()
        list = List.objects.get(pk=card.list.id)
        project = Project.objects.get(pk=list.project.id)
        if ((request.user.role == 'n') and not project.member.filter(id=request.user.id).exists()):
            return HttpResponse(
                "You dont have permission to update card in this project.")
        return super().update(request, *args, **kwargs)
   
