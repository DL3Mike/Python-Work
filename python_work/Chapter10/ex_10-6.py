# Write a program that prompts for two numbers. Add them together and print the results.
# Cath the ValueError if either input value is not a number, and print a friendly
# error message.
print("Give me two numbers and I'll add them.")
print("(Enter 'q' to Quit.)")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can only enter number values!")
    else:
        print(answer)
