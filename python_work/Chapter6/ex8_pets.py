pet_0 = {'animal': 'dog', 'owner': 'bob'}
pet_1 = {'animal': 'cat', 'owner': 'sally'}

pets = [pet_0, pet_1]

for pet in pets:
    print(
        f"The pet is a {pet['animal']}. The owner is {pet['owner'].title()}.")
