# A tuple's value cannot be changed once defined & tuples use '()' instead of '[]'
dimensions = (200, 50)

foods = ('pizza', 'pasta', 'rice', 'corn', 'bread')

for food in foods:
    print(food)

# Does not work
# foods[0] = 'water'

# Does Work, u can only redefine the tuple!
foods = ('water', 'coke', 'rice', 'corn', 'bread')
