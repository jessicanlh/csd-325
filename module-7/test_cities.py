import unittest
from city_functions import format_city_country

#tests for the function
class TestCities(unittest.TestCase):
    def test_format_city_country(self): #test if function works correctly
        result = format_city_country("San Francisco", "US")
        self.assertEqual(result, "San Francisco, US")

if __name__ == '__main__':
    unittest.main()