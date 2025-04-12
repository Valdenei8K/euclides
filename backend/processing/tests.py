from django.db.models.expressions import result
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.test import TestCase

from processing.services.calculator_service import CalculatorService


class NumeroEndpointTest(APITestCase):

    def test_post_numeros(self):
        url = reverse('processar')
        data = {'numeros': [5, 10, 15]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertTrue(isinstance(response.data['id'], int))
        self.assertIn('media', response.data)
        self.assertIn('mediana', response.data)
        self.assertEqual(response.data['media'], None)
        self.assertEqual(response.data['mediana'], None)

    def test_empty_list(self):
        url = reverse('processar')
        data = {'numeros': []}
        response = self.client.post(url, data, format='json')
        expected = {'numeros': ['Ensure this field has at least 3 elements.']}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(expected, response.json())


    def test_get_numeros(self):
        url = reverse('processar')
        data = {'numeros': [5, 10, 15]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        url = reverse('listar')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreater(len(response.data),0)




class CalculatorServiceTestCase(TestCase):

    def test_calculate_median_3_numbers(self):
        numbers = [5,10,15]
        result = CalculatorService.calculate_median(numbers)
        self.assertEqual(result, 10)

    def test_calculate_median_numbers_even(self):
        numbers = [5, 13, 17, 30]
        result = CalculatorService.calculate_median(numbers)
        self.assertEqual(result, 15)

    def test_calculate_median_numbers_odd(self):
        numbers = [63, 95, 3, 19, 2]
        result = CalculatorService.calculate_median(numbers)
        self.assertEqual(result, 19)

    def test_calculate_average_3_numbers(self):
        numbers = [65, 15, 19]
        result = CalculatorService.calculate_average(numbers)
        self.assertEqual(result, 33)

    def test_calculate_average_4_numbers(self):
        numbers = [55, 403, 6, 69]
        result = CalculatorService.calculate_average(numbers)
        self.assertEqual(result, 133.25 )