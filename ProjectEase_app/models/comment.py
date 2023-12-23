from django.db import models
from ckeditor.fields import RichTextField
from .card import Card
from .user import User
from django.utils import timezone

class Comment(models.Model):
    text=RichTextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='comments')
    created_at = models.DateTimeField(default=timezone.now)
    card=models.ForeignKey(Card,on_delete=models.CASCADE,related_name='comments')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.author}({self.text})'

#done