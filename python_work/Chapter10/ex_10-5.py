# Write a while loop that asks users what like about code
# Store the values in in a files that adds all their responses on a new line
filename = 'chapter10/responses.txt'

prompt = "Whats your favorite thing about coding?\n"
prompt += "(Enter 'q' to Quit.)"

while True:
    response = input(prompt)

    if response.lower() == 'q':
        break
    else:
        with open(filename, 'a') as responseList:
            responseList.write(f"{response}\n")
