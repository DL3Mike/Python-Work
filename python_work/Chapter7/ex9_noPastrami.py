sandwhich_orders = ['pastrami', 'chicken',
                    'tuna', 'pastrami', 'hamburger', 'pastrami']
finished_sandwhiches = []

print("The deli has ran out of pastrami sandwhiches")
while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    sandwhich = sandwhich_orders.pop()
    print(f"I made your {sandwhich} sandwhich.")

    finished_sandwhiches.append(sandwhich)

print("Finished Orders:")
for sandwhich in finished_sandwhiches:
    print(f"{sandwhich}")
