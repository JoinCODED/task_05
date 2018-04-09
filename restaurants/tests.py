from django.test import TestCase
from django.urls import reverse
from restaurants.models import Restaurant

class RestarantModelTestCase(TestCase):
    def test_create(self):
        Restaurant.objects.create(
            name="Hamza's Pizza",
            description="Pizza that tastes really good.",
            opening_time="00:01:00",
            closing_time="23:59:00"
            )

class RestaurantViewTestCase(TestCase):
    def test_welcome_view(self):
        url = reverse("hello-world")
        response = self.client.get(url)
        self.assertIn("Hello World!", response.context['msg'])
        self.assertContains(response, "Hello World!")
        self.assertEqual(response.status_code, 200)

    def test_list_view(self):
        list_url = reverse("restaurant-list")
        response = self.client.get(list_url)
        self.assertTrue(isinstance(response.context['my_list'],list))
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        detail_url = reverse("restaurant-detail")
        response = self.client.get(detail_url)
        self.assertTrue(isinstance(response.context['my_object'],dict))
        self.assertTemplateUsed(response, 'detail.html')
        self.assertEqual(response.status_code, 200)
