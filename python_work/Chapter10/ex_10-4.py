# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.
filename = 'chapter10/guest_book.txt'

prompt = "\nWhats your Name?"
prompt += "\n(Enter 'q' to Quit.)"

while True:
    name = input(prompt)

    if name.lower() == 'q':
        break
    else:
        with open(filename, 'a') as guestbook:
            guestbook.write(f"{name} Checked in at 9/18/23\n")
            print(f"Greetings {name}, enjoy the stay!")

print("Thank you for visiting!")
