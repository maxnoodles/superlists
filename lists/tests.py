from django.test import TestCase

# Create your tests here.
class Smoketest(TestCase):
     def test_bad_maths(self):
         self.assertEqual(1+1, 3)


