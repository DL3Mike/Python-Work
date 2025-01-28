for number in range(1, 21):
    print(number)
list_of_numbers = list(range(1, 1000001))
print("\n")
print(min(list_of_numbers))
print(max(list_of_numbers))
print(sum(list_of_numbers))
print("\n")

list_of_odd_numbers = list(range(1, 21, 2))
for odd_number in list_of_odd_numbers:
    print(odd_number)
print("\n")

list_of_three_numbers = list(range(3, 34, 3))
for three_number in list_of_three_numbers:
    print(three_number)
print("\n")

cube_list = [n ** 3 for n in range(1, 11)]
for cube in cube_list:
    print(cube)
