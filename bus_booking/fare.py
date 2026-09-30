from .routes import BASE_FARE, get_route

def calculate_fare(route_id, age):
    #Calculate fare using route distance and age-based discount.
    route = get_route(route_id)
    fare = BASE_FARE + route["distance"] * route["rate"]

    if age < 12:
        fare = fare*0.50
    elif age >= 60:
        fare = fare*0.80

    return round(fare, 2)
