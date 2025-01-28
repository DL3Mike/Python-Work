favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'paul', 'edward']

for person in people:
    if person in favorite_language.keys():
        print(f"Thank you {person.title()} for responding to our survey!")
    else:
        print(f"Hey {person.title()}, You should come take our survey.")
