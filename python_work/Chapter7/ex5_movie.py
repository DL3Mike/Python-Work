prompt = "What is your age?"
prompt += "(Type 'end' when your done buying tickets.)"

while True:
    age = input(prompt)

    if age == 'end':
        break
    else:
        int_age = int(age)
        if int_age < 3:
            price = 0
        elif int_age < 13:
            price = 10
        else:
            price = 15

        print(f"Your ticket is ${price}")
