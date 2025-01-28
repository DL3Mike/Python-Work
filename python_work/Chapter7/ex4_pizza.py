prompt = "What toppings would you like?"
prompt += "(Type 'quit' to stop)"

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Ill add {topping} to your pizza.")
