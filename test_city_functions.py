#test case for tiy_city_funcitons

import unittest

from tiy_city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """Test for tiy_city_function.py"""
    def test_city_country(self):
        """Do City, Country names like 'Nairobi, Kenya.' work?"""
        name_formatted = get_city_country('nairobi', 'kenya')
        self.assertEqual(name_formatted, 'Nairobi, Kenya')

    def test_city_country_population(self):
        """Do City, Country Population like 'Lagos, Nigeria - Population 70000' work?"""
        name_formatted = get_city_country('lagos', 'nigeria', 70000)
        self.assertEqual(name_formatted, 'Lagos, Nigeria - Population 70000.')
        

unittest.main()