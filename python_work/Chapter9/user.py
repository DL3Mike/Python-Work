class User:
    """Create a User class"""

    def __init__(self, first_name, last_name, age, height, race):
        """Initilize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.race = race
        self.login_attempts = 0

    def describe_user(self):
        """Display user information"""
        print(f"{self.first_name} {self.last_name}:")
        print(f"{self.age} Years old")
        print(f"{self.height}FT tall")
        print(f"{self.race} Ethnicity")

    def greet_user(self):
        """Print personilzed greeting to user"""
        print(
            f"Welcome {self.first_name.title()}, glad to meet you we are both {self.age} years old.\n")

    def increment_login_attemps(self):
        """Increment login attempt by 1"""
        self.login_attempts += 1
        print(
            f"{self.first_name}, you have attemepted a login {self.login_attempts} times now!")

    def reset_login_attempts(self):
        """Resets login attempts to zero"""
        self.login_attempts = 0
        print(
            f"{self.first_name.title()}, your login attempt has been reset to {self.login_attempts}\n")


class Privileges:
    """Create a model for privileges"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Display user privileges"""
        print("Admin privileges are:")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    """Initilize attributes from parent class"""

    def __init__(self, first_name, last_name, age, height, race, privileges):
        """Initilize attributes of parent class"""
        super().__init__(first_name, last_name, age, height, race)
        self.privileges = Privileges(privileges)


user_1 = User('michael', 'davis', 22, 6, 'African American')
user_2 = Admin('darry', 'benton', 19, 5, 'mexican',  [
    'Can add post', 'can delete post', 'can ban users'])
user_3 = User('chaeuse', 'pryor', 18, 5, 'white')

user_1.describe_user()
user_1.greet_user()
print("---")
user_1.increment_login_attemps()
user_1.increment_login_attemps()
user_1.increment_login_attemps()
print("----")
user_1.reset_login_attempts()

user_2.privileges.show_privileges()
