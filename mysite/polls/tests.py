from django.test import TestCase
import xmlrunner

# Create your tests here.
class mathTestCase(TestCase):
    def test_divide(self):
        self.assertEqual(1, (100/100))

    def test_minus(self):
        self.assertEqual(1, (2-1))

    def test_plus(self):
        self.assertEqual(1, (1+0))

if __name__ == '__main__':
    TestCase.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)
