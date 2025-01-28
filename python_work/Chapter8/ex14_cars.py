def make_car(manufacturer, model, **specs):
    """build a dictionary containing everything we know about a car"""
    specs['manufacturer'] = manufacturer
    specs['model'] = model
    return specs


car = make_car('Chevy', 'malibu', color='blue', tow_package=True)
print(car)
