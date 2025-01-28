responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("What is your dream vaction?")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (y/n)")
    if repeat == 'n':
        polling_active = False

print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name}'s dream vacation is {response}")
