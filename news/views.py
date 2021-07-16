from .models import Post, Upvote
from .serializers import PostSerializer
from rest_framework import generics,permissions
from rest_framework import viewsets
from .mixins import UpvoteMixin


class AuthorPostList(generics.ListCreateAPIView):
    """List of posts created by user
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.kwargs['author'])


class PostViewSet(viewsets.ModelViewSet, UpvoteMixin):
    """CRUD operations on posts and upvotes
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)