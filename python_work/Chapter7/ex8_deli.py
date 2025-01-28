sandwhich_orders = ['chicken', 'tuna', 'hamburger']
finished_sandwhiches = []

while sandwhich_orders:
    sandwhich = sandwhich_orders.pop()
    print(f"I made your {sandwhich} sandwhich.")

    finished_sandwhiches.append(sandwhich)

print("Finished Orders:")
for sandwhich in finished_sandwhiches:
    print(f"{sandwhich}")
