from django.test import TestCase
from restaurant.models import Menu, Booking

class MenuModelTest(TestCase):
    def test_create_menu(self):
        item = Menu.objects.create(title="Pizza", price=10, inventory=5)
        self.assertEqual(item.title, "Pizza")

class BookingModelTest(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(name="John", no_of_guests=2)
        self.assertEqual(booking.name, "John")
