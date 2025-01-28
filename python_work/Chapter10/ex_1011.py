# Write a program that prompts for the user's favorite number. Use json.dump()
# to store this number in a file. Write a seperate program that reads in this value
# and prints the message, "I know your favorite number! It's ___."
import json

filename = 'chapter10/fav_num.json'


with open(filename) as f:
    fav_num = json.load(f)
    print(f"I know your favorite number! It's {fav_num}")
