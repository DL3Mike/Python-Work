class Restaurant:
    """Create a restaurant model"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initilize restaurent name and cuisine attribute"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant information"""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints open message"""
        print(f"{self.restaurant_name} is open for business!")

    def set_number_served(self, guests):
        """sets number of guess served"""
        self.number_served = guests

    def increment_number_served(self, increment):
        """Incriments guests number served"""
        self.number_served += increment
