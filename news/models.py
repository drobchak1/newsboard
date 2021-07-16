from django.db import models
from newsboard import settings
from django.contrib.contenttypes.fields import (
    GenericRelation,
    GenericForeignKey,
)
from django.contrib.contenttypes.models import ContentType


class Upvote(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="upvotes",
        on_delete=models.CASCADE,
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    date_of_creation = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.CharField(max_length=120)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
    )
    upvotes = GenericRelation(Upvote)
    amount_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    @property
    def total_upvotes(self):
        return self.upvotes.count()
