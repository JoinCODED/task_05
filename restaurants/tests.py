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
    def setUp(self):
        self.restaurant_1 = Restaurant.objects.create(name="Restaurant 1", description="This is Restaurant 1", opening_time="00:01:00", closing_time="23:59:00")
        self.restaurant_2 = Restaurant.objects.create(name="Restaurant 2", description="This is Restaurant 2", opening_time="00:01:00", closing_time="23:59:00")
        self.restaurant_3 = Restaurant.objects.create(name="Restaurant 3", description="This is Restaurant 3", opening_time="00:01:00", closing_time="23:59:00")

    def test_welcome_view(self):
        url = reverse("hello-world")
        response = self.client.get(url)
        self.assertIn("Hello World!", response.context['msg'])
        self.assertContains(response, "Hello World!")
        self.assertEqual(response.status_code, 200)

    def test_list_view(self):
        list_url = reverse("restaurant-list")
        response = self.client.get(list_url)
        for restaurant in Restaurant.objects.all():
            self.assertIn(business, response.context['restaurants'])
            self.assertContains(response, restaurant.name)
            self.assertContains(response, restaurant.description)
            self.assertContains(response, restaurant.opening_time)
            self.assertContains(response, restaurant.closing_time)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        detail_url = reverse("restaurant-detail", kwargs={"restaurant_id":self.restaurant_1.id})
        response = self.client.get(detail_url)
        self.assertEqual(self.restaurant_1, response.context['restaurant'])
        self.assertContains(response, self.restaurant_1.name)
        self.assertContains(response, self.restaurant_1.description)
        self.assertContains(response, restaurant_1.opening_time)
        self.assertContains(response, restaurant_1.closing_time)
        self.assertTemplateUsed(response, 'detail.html')
        self.assertEqual(response.status_code, 200)
