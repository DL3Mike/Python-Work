class Employee:
    """Create a Employee class that stores name and salary"""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, bonus=5000):
        self.annual_salary += bonus
