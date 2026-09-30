from .routes import ROUTES, TOTAL_SEATS
from .fare import calculate_fare
from .booking import BookingManager
from .display import display_routes, show_available_seats, show_ticket
from .input_utils import read_int

def book_seat(manager):
    display_routes(ROUTES, manager)
    route_id = read_int("\nEnter route ID: ", 1, len(ROUTES))

    if manager.available_seats(route_id) == 0:
        print("Sorry, this bus is full.")
        return

    show_available_seats(manager, route_id)
    seat = read_int("Choose seat number: ", 1, TOTAL_SEATS)

    name = input("Passenger name: ").strip()
    if not name:
        print("Passenger name cannot be empty.")
        return

    age = read_int("Age: ", 1, 120)
    phone = input("Phone: ").strip()

    fare = calculate_fare(route_id, age)
    success, result = manager.book(route_id, seat, name, age, phone, fare)

    if not success:
        print(result)
        return

    ticket_id = result
    show_ticket(ticket_id, manager.bookings[ticket_id], ROUTES[route_id])

def cancel_booking(manager):
    ticket_id = read_int("Enter ticket ID to cancel: ")
    success, result = manager.cancel(ticket_id)

    if not success:
        print("No booking found with that ticket ID.")
        return

    print(f"Ticket {ticket_id} cancelled. Refund: Rs. {result} (10% cancellation charge)")

def search_passenger(manager):
    key = input("Enter passenger name or ticket ID: ").strip()
    found = manager.search(key)

    if not found:
        print("No passenger found.")
        return

    print("\nTicket  Name            Age  Route                 Seat  Fare")
    print("-" * 65)
    for ticket_id, booking in found:
        route = ROUTES[booking["route"]]
        route_name = f"{route['source']}->{route['destination']}"
        print(f"{ticket_id:<8}{booking['name']:<16}{booking['age']:<5}"
              f"{route_name:<22}{booking['seat']:<6}Rs. {booking['fare']}")

def fare_calculator():
    display_routes(ROUTES, BookingManager(ROUTES, TOTAL_SEATS))
    route_id = read_int("\nEnter route ID: ", 1, len(ROUTES))
    age = read_int("Passenger age: ", 1, 120)
    print(f"Estimated fare: Rs. {calculate_fare(route_id, age)}")

def run():
    manager = BookingManager(ROUTES, TOTAL_SEATS)
    actions = {
        1: lambda: display_routes(ROUTES, manager),
        2: lambda: book_seat(manager),
        3: lambda: cancel_booking(manager),
        4: lambda: search_passenger(manager),
        5: fare_calculator,
    }

    while True:
        print("""
====== BUS BOOKING SYSTEM ======
1. Display routes
2. Book a seat
3. Cancel booking
4. Search passenger
5. Calculate fare
6. Exit
""")
        choice = read_int("Choice: ", 1, 6)

        if choice == 6:
            print("Thank you! Have a safe journey.")
            break
        actions[choice]()

if __name__ == "__main__":
    run()
