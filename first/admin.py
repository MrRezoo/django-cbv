from django.contrib import admin

# Register your models here.
from first.models import Todo, Comment

admin.site.register(Todo)
admin.site.register(Comment)
