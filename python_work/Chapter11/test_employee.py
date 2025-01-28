import unittest
from employee_function import Employee


class TestEmployeeFunction(unittest.TestCase):
    """ Tests for the class Employee """

    def setUp(self):
        """Create a set of employee to test raise method"""
        self.employee_1 = Employee('John', 'Davis', 70000)
        self.employee_2 = Employee('Martha', 'Stewart', 60000)

    def test_give_default_raise(self):
        """ Test if the default raise works  """
        # Give employee default raise.
        self.employee_1.give_raise()
        # Check if employe default raise updated correctly
        self.assertEqual(self.employee_1.annual_salary, 70000 + 5000)

    def test_give_custom_raise(self):
        """ Test if the default raise works  """
        # Give employee default raise.
        self.employee_2.give_raise(10000)
        # Check if employe default raise updated correctly
        self.assertEqual(self.employee_2.annual_salary, 60000 + 10000)


if __name__ == '__main__':
    unittest.main()
