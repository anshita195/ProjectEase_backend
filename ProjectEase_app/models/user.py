from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    user_role = [
        ('a', 'admin'),
        ('n', 'normal_user')
    ]
    
    name = models.CharField(max_length=60)
    year = models.IntegerField(null=True,blank=True)
    enabled=models.BooleanField(default=True)
    role=models.CharField(max_length=1,choices=user_role,default='n')
    email=models.EmailField(max_length=60)
    enrollment_no=models.BigIntegerField(unique=True,null=True,blank=True)
    image=models.CharField(null=True,blank=True,max_length=400)

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=_('groups'),
    #     blank=True,
    #     related_name='custom_user_groups'  # Add a related_name
    # )

    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=_('user permissions'),
    #     blank=True,
    #     related_name='custom_user_permissions'  # Add a related_name
    # )
 
    class Meta:
        unique_together=('name','enrollment_no')