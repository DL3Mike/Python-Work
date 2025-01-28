rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'north america',
}

for river, country in rivers.items():
    print(f"\nThe {river.title()} river runs through {country.title()}")

for river in rivers:
    print(f"\nThe {river.title()} river.")

for country in rivers.values():
    print(f"\nCountry:{country.title()}.")
