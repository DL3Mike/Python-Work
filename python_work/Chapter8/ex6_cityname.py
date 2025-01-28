def city_country(city, country):
    """Return formated city, country name."""
    return f"{city.title()}, {country.title}"


print(city_country("chattanooga", "Tennessee"))
print(city_country("Red bank", "tennessee"))
print(city_country("london", "england"))
