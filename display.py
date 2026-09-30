from .routes import TOTAL_SEATS

def display_routes(routes, booking_manager):
    print("\nID  From       To           Km   Rs/Km   Seats Free")
    print("-" * 55)
    for route_id, route in routes.items():
        free = booking_manager.available_seats(route_id)
        print("route_id:", route_id, "  ", route['source'], "  ", route['destination'], "  ", route['distance'], "  ", route['rate'], "  ", free)
              

def show_available_seats(booking_manager, route_id):
    booked = booking_manager.seats[route_id]
    print("Seats (X = booked):")
    for seat in range(1, TOTAL_SEATS + 1):
        if seat in booked:
            print("X", end=" ")
        else:
            print(seat, end=" ")
        if seat % 4 == 0:
            print()

def show_ticket(ticket_id, booking, route):
    print("========== TICKET CONFIRMED =========")
    print("Ticket ID : ",ticket_id)
    print("Passenger : ",booking['passenger'])
    print("age       : ",booking['age'])
    print("Route     : ",route['source'] + " to " + route['destination'])
    print("Distance  : ",route['distance'],"Km")
    print("seat      : ",booking['seat'])
    print("Total Fare: Rs.",route['distance'] * route['rate'])
    print("=====================================")
