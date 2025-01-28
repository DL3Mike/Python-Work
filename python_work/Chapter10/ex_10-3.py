# Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt.
filename = 'chapter10/guest.txt'

name = input("What is your name?")

with open(filename, 'a') as guestList:
    guestList.write(f'{name}\n')

with open(filename) as guestList:
    contents = guestList.read()
print(contents)
