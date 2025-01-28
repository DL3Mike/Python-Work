person1 = {
    'first_name': 'kamia',
    'last_name': 'williams',
    'age': 16,
    'city': 'chattanooga',
}
person2 = {
    'first_name': 'darry',
    'last_name': 'benton',
    'age': 19,
    'city': 'chattanooga',
}
person3 = {
    'first_name': 'dominique',
    'last_name': 'strickland',
    'age': 13,
    'city': 'chattanooga',
}

people = [person1, person2, person3]

for person in people:
    for k, v in person.items():
        print(f"{k}: {v}")
    print("\n")
