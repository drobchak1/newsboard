from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CommentTests(APITestCase):
    def test_get_comment_list(self):
        """
        Ensure we can get list of comments.
        """
        url = reverse("comment-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
