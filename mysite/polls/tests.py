from django.test import TestCase

# Create your tests here.
class mathTestCase(TestCase):
    def test_divide(self):
        self.assertEqual(1, (100/100))

    def test_minus(self):
        self.assertEqual(1, (2-1))
