random_list = ['peperoni', 'cheese', 'supreme', 'shark', 'whale',
               'dolphin', 'Lebron James', 'Martin Luther King Jr', 'Bill Gates']
print('The first three items in the list are pizzas:')
for pizza in random_list[:3]:
    print(pizza)

print('\nThree items from the middle of the list are sea animals:')
for sea_animal in random_list[3:6]:
    print(sea_animal)

print('\nThe last three items in the list are people:')
for people in random_list[-3:]:
    print(people)

pizza_list = ['peperoni', 'cheese', 'supreme']
friend_pizza = pizza_list[:]
friend_pizza.append('meatlover')
for pizzas in friend_pizza:
    print(f'My favorite pizzas are: {pizzas}')

for pizzas in pizza_list:
    print(f"My friend's favorite pizzas are: {pizzas}")
