from django.contrib import admin
from .models import Post, Upvote

# Register your models here.

admin.site.register(Post)
admin.site.register(Upvote)
