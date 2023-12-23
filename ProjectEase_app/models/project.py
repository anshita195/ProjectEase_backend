from django.db import models
from ckeditor.fields import RichTextField
from .user import User


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    wiki = RichTextField(null=True, blank=True)
    member = models.ManyToManyField(
        User, related_name='projects')
    locked = models.BooleanField(default=False)
    github_link = models.URLField(null=True, blank=True)
    year1_visibility=models.BooleanField(default=True)
    year2_visibility=models.BooleanField(default=True)
    year3_visibility=models.BooleanField(default=True)
    year4_visibility=models.BooleanField(default=True)
    year5_visibility=models.BooleanField(default=True)



    def __str__(self):
        return f' {self.name}()'

    


