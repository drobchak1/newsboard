from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from .models import Upvote, Post

User = get_user_model()


def add_upvote(obj, user):
    """Upvote post."""
    obj_type = ContentType.objects.get_for_model(obj)
    upvote, is_created = Upvote.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    Post.objects.filter(id=obj.id).update(
        amount_of_upvotes=F("amount_of_upvotes") + 1
    )
    return upvote


def remove_upvote(obj, user):
    """Remove Upvote from post."""
    obj_type = ContentType.objects.get_for_model(obj)
    Upvote.objects.filter(
        content_type=obj_type, object_id=obj.id, user=user
    ).delete()
    Post.objects.filter(id=obj.id).update(
        amount_of_upvotes=F("amount_of_upvotes") - 1
    )


# def is_fan(obj, user) -> bool:
#     """Check if user upvoted post
#     """
#     if not user.is_authenticated:
#         return False
#     obj_type = ContentType.objects.get_for_model(obj)
#     upvotes = Upvote.objects.filter(
#         content_type=obj_type, object_id=obj.id, user=user)
#     return upvotes.exists()


def get_fans(obj):
    """Get all users, who upvoted post"""
    obj_type = ContentType.objects.get_for_model(obj)
    return User.objects.filter(
        upvotes__content_type=obj_type, upvotes__object_id=obj.id
    )
