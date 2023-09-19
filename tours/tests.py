from django.test import TestCase
from .models import Tour
# Create your tests here.

class TourModelTest(TestCase):
    def setUp(self):
        Tour.objects.create(name='Test Tour', description='Test Description', start_date='2023-09-20', end_date='2023-09-25')

    def test_tour_name(self):
        tour = Tour.objects.get(id=1)
        self.assertEqual(str(tour), 'Test Tour')

# run the test using python manage.py test