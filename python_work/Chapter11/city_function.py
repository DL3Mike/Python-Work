# Write a function that accepts two parameters: a city name and state name.
# The function should return a single string of the form City, State.
# Store the function in a module called city_functions.py

def get_formated_cityState_name(city, state, population=''):
    """Generate City & State name"""
    if population:
        city_state_name = f"{city}, {state} - population {population}."
    else:
        city_state_name = f"{city} {state}"
    return city_state_name.title()
