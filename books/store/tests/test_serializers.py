from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test Book 1', price=600.00)
        book_2 = Book.objects.create(name='Test Book 2', price=800.00)
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'name': 'Test Book 1',
                'price': '600.00'
            },
            {
                'name': 'Test Book 2',
                'price': '800.00'
            }
        ]
        self.assertEqual(expected_data, data)
