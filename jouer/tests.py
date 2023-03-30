from django.test import TestCase
from views import getMot
#test unitaire
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method
        pass

    def tearDown(self):
        # Clean up run after every test method
        pass

    def test_getMot_function(self):
        mot = getMot()
        self.assertFalse(len(mot) == 0)
