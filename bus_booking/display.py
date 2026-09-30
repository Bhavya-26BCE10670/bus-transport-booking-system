from .routes import TOTAL_SEATS

def display_routes(routes, booking_manager):
    print("\nID  From       To           Km   Rs/Km   Seats Free")
    print("-" * 55)
    for route_id, route in routes.items():
        free = booking_manager.available_seats(route_id)
        print(f"{route_id:<3} {route['source']:<10} {route['destination']:<12} "
              f"{route['distance']:<4} {route['rate']:<7} {free}")

def show_available_seats(booking_manager, route_id):
    booked = booking_manager.seats[route_id]
    print("\nSeats (X = booked):")
    for seat in range(1, TOTAL_SEATS + 1):
        print(" X  " if seat in booked else f"{seat:>2}  ", end="")
        if seat % 4 == 0:
            print()

def show_ticket(ticket_id, booking, route):
    print("\n===== TICKET CONFIRMED =====")
    print(f"Ticket ID : {ticket_id}")
    print(f"Passenger : {booking['name']} (Age {booking['age']})")
    print(f"Route     : {route['source']} -> {route['destination']}")
    print(f"Seat No.  : {booking['seat']}")
    print(f"Fare      : Rs. {booking['fare']}")
    print("============================")
