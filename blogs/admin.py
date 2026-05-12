
from django.contrib import admin
from .models import BlogsModel,CommentModel

# Register your models here.
admin.site.register(BlogsModel)
admin.site.register(CommentModel)
