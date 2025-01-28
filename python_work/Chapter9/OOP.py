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


class IceCreamStand(Restaurant):
    """Inititials attributes of class parent """

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Iniitilize attributes of parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavor(self):
        """display flavor"""
        print(f"The flavors are:")
        for flavor in self.flavors:
            print(f"-{flavor}")


pizza_store = Restaurant('Papa Johns', 'Pizza')
pizza_store.describe_restaurant()
pizza_store.open_restaurant()

print(pizza_store.number_served)
pizza_store.set_number_served(5)
print(pizza_store.number_served)
print("-----")
pizza_store.increment_number_served(10)
print(pizza_store.number_served)

ice_cream = IceCreamStand('ice cream parlor', 'ice cream', [
                          'chocolate', 'strawberry', 'vanilla'])
ice_cream.describe_restaurant()
ice_cream.display_flavor()
