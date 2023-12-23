from django.db import models
from ckeditor.fields import RichTextField
from .user import User
from .list import List
from django.utils import timezone


class Card(models.Model):
    priority_choices = [
        ('h', 'high'),
        ('m', 'medium'),
        ('l', 'low'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    assignees = models.ManyToManyField(User)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.CharField(
        choices=priority_choices, max_length=1, null=True, blank=True)
    is_resolved = models.BooleanField(null=True, blank=True,default=False)
    description = RichTextField()
    list = models.ForeignKey(
        List, on_delete=models.CASCADE, related_name='cards')

    

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'list')

# done
