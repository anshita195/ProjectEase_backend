from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Project)
admin.site.register(Card)
admin.site.register(List)
admin.site.register(Project_role)

# Register your models here.
