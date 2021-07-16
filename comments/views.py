from .models import Comment
from .serializers import CommentSerializer
from rest_framework import permissions
from rest_framework import viewsets

# Create your views here.


class CommentViewSet(viewsets.ModelViewSet):
    """CRUD operations on posts and upvotes"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
