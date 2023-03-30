from django.test import TestCase
from . import views
#test unitaire
class YourTestClass(TestCase):
    def setUp(self):
        # Setup run before every test method
        pass

    def tearDown(self):
        # Clean up run after every test method
        pass

    def test_getMot_function(self):
        mot = views.getMot()
        print(len(mot))
        print("test" + mot + "test")
        self.assertFalse(len(mot) == 0)
