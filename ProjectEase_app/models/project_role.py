from django.db import models
from ckeditor.fields import RichTextField
from .user import User
from .project import Project


class Project_role(models.Model):
    choices = [
        ('l', 'leader'),
        ('m', 'member')
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    project_role = models.CharField(max_length=1, choices=choices)

# str method left
