favorite_places = {
    'logan': ['china', 'brazil', 'japan'],
    'step': ['jackson', 'daya', 'gas'],
    'keith': ['camera', 'memphis', 'taylor'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")
    print("\n")
