from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class LeapYearTests(APITestCase):
    def test_check_leap_year_true(self):
        url = reverse('check_leap_year', args=[2020])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'year': 2020, 'is_leap': True})

    def test_check_leap_year_false(self):
        url = reverse('check_leap_year', args=[2019])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'year': 2019, 'is_leap': False})

    def test_check_leap_year_range(self):
        url = reverse('check_leap_year_range', args=[2000, 2020])
        response = self.client.get(url)
        expected_data = {
            'start_year': 2000,
            'end_year': 2020,
            'leap_years': [2000, 2004, 2008, 2012, 2016, 2020]
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected_data)

    def test_history(self):
        # Create some history entries by calling other endpoints
        self.client.get(reverse('check_leap_year', args=[2020]))
        self.client.get(reverse('check_leap_year_range', args=[2000, 2020]))

        url = reverse('history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('history' in response.json())
        self.assertGreater(len(response.json()['history']), 0)
