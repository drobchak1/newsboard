from rest_framework.decorators import action
from rest_framework.response import Response
from news import services
from users.serializers import UserSerializer


class UpvoteMixin:
    @action(detail=True, methods=["post"])
    def upvote(self, request, pk=None):
        """Upvote post."""
        obj = self.get_object()
        services.add_upvote(obj, request.user)
        print(self)
        return Response()

    @action(detail=True, methods=["post"])
    def unupvote(self, request, pk=None):
        """Unupvote post."""
        obj = self.get_object()
        services.remove_upvote(obj, request.user)
        obj.amount_of_upvotes -= 1
        return Response()

    @action(detail=True, methods=["get"])
    def fans(self, request, pk=None):
        """Get all people, who upvoted post."""
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = UserSerializer(fans, many=True)
        return Response(serializer.data)
