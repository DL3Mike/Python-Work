import unittest
from city_function import get_formated_cityState_name


class CityTestCase(unittest.TestCase):
    """Tests for 'city_function.py' """

    def test_city_state(self):
        """Do names like chattanooga tennessee work?"""
        formatted_name = get_formated_cityState_name(
            'chattanooga', 'tennessee')
        self.assertEqual(formatted_name, 'Chattanooga Tennessee')

    def test_city_state_population(self):
        """Does population status work?"""
        formatted_name = get_formated_cityState_name(
            'jackson', 'tennessee', 5000
        )
        self.assertEqual(
            formatted_name, 'Jackson, Tennessee - Population 5000.')


if __name__ == '__main__':
    unittest.main()
