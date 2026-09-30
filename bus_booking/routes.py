TOTAL_SEATS = 40
BASE_FARE = 50

ROUTES = {
    1: {"source": "Ashta", "destination": "Bhopal", "distance": 75, "rate": 1.5},
    2: {"source": "Ashta", "destination": "Indore", "distance": 100, "rate": 1.6},
    3: {"source": "Bhopal", "destination": "Indore", "distance": 190, "rate": 1.5},
    4: {"source": "Indore", "destination": "Ujjain", "distance": 55, "rate": 1.4},
    5: {"source": "Bhopal", "destination": "Jabalpur", "distance": 330, "rate": 1.3},
}

def get_route(route_id):
    return ROUTES[route_id]

def route_is_valid(route_id):
    return route_id in ROUTES
