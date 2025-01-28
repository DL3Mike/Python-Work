car = 'subaru'
print("Is car == 'Subaru'? I predict True")
print(car == 'subaru')
print("Is car == 'ford'? I predict True")
print(car == 'ford')

requested_topping = 'pepperoni'
if requested_topping != 'sausage':
    print("No Sausage!")

building = 'JCM'
print("If building == 'jcm' is false its case-sensitive")
print(building == 'jcm')
print("If building == 'jcm' is true its no longer case-sensitive")
print(building.lower() == 'jcm')

zoey = 22
candace = 19
if zoey > candace:
    print("Zoey is older than Candace")
