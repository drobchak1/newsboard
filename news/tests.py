from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User
from news.models import Post


class PostTests(APITestCase):
    def test_get_post_list(self):
        """
        Ensure we can get list of posts.
        """
        url = reverse("post-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_create(self):
        """
        Ensure we can register user and create post using JWT-token.
        """
        url = reverse("token_obtain_pair")
        User.objects.create_user(username="user", password="user12345")
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "user")

        resp = self.client.post(
            url, {"email": "user", "password": "user12345"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        resp = self.client.post(
            url, {"username": "user", "password": "user12345"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in resp.data)
        self.assertTrue("refresh" in resp.data)
        token = resp.data["access"]

        verification_url = reverse("post-list")

        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION="Bearer " + "abc")
        resp = client.post(
            verification_url,
            {
                "title": "news",
                "link": "https://www.theguardian.com/international",
            },
        )
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        client.credentials(HTTP_AUTHORIZATION="Bearer " + token)
        resp = client.post(
            verification_url,
            {
                "title": "news",
                "link": "https://www.theguardian.com/international",
            },
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "news")
