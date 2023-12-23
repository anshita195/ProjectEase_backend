from django.db import models
from .project import Project
from ProjectEase_app.utils import generate_unique_colour
import secrets



class List(models.Model):
    id = models.AutoField( primary_key=True)
    name=models.CharField(max_length=40)
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='lists')
    color=models.CharField(max_length=7,default=generate_unique_colour)

    def __str__(self):
        return self.name
    
   
                

    class Meta:
        unique_together=('name','project')
        ordering=['id']