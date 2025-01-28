favorite_number = {
    'maurice': [3, 5],
    'braven': [2, 7],
    'ceecee': [0, 6, 8],
}

for name, numbers in favorite_number.items():
    print(f"{name.title()}:")
    for num in numbers:
        print(f"{num}")
    print("\n")

#print(f"Maurice favorite number is {favorite_number['maurice']}.")
#print(f"Braven favorite number is {favorite_number['braven']}.")
#print(f"Ceecee favorite number is {favorite_number['ceecee']}.")
