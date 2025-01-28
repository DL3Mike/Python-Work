filename = 'chapter10/learning_python.txt'

# with open(filename) as file_object:
#    contents = file_object.read()
# print(contents)

# print("\n")

#
# with open(filename) as file_object:
#    for line in file_object:
#        print(line)
#

pi_string = ''
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
