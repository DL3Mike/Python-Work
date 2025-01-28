cities = {
    'chattanooga': {
        'state': 'tennessee',
        'population': 200000,
        'fact': 'Scenic city',
    },
    'tempe': {
        'state': 'arizona',
        'population': 5000000,
        'fact': 'dessert of a city',
    },
    'huntsville': {
        'state': 'alabama',
        'population': 1000000,
        'fact': 'country city',
    },
}

for city, info in cities.items():
    print(
        f"City of {city.title()} is in the state of {info['state'].title()}, has a population of {info['population']}")
    print(f"And a fun fact: {info['fact']}\n")

# for city, info in cities.items():
#    print(f"City of {city.title()} Info:")
#    for k, v in info.items():
#       print(f"{k.title()}: {v}")
#    print("\n")
