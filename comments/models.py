from django.db import models
from newsboard import settings
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    content = models.CharField(max_length=120)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('news.Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content