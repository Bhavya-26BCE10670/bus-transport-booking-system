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
    print("booking canceled successfully.")

def search_passenger(manager):
    key = input("Enter passenger name or ticket ID: ").strip()
    found = manager.search(key)

    if not found:
        print("No passenger found.")
        return

    print("Ticket  Name            Age  Route                 Seat  Fare")
    print("-------------------------------------------------------------")
    for ticket_id, booking in found:
        route = ROUTES[booking["route"]]
        route_name = f"{route['source']}->{route['destination']}"
        print("ticket", ticket_id, booking["name"].ljust(15), str(booking["age"]).ljust(4), route_name.ljust(20), str(booking["seat"]).ljust(5), f"Rs. {booking['fare']}")
def fare_calculator():
    display_routes(ROUTES, BookingManager(ROUTES, TOTAL_SEATS))
    route_id = read_int("Enter route ID: ", 1, len(ROUTES))
    age = read_int("Passenger age: ", 1, 120)
    print("fare: Rs.", calculate_fare(route_id, age))


while True:
    print("************** Bus Booking System ********************")
    print("1. View Routes")
    print("2. Book a Seat")
    print("3. Cancel Booking")
    print("4. Search Passenger")
    print("5. Fare Calculator")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_routes(ROUTES, manager)
    elif choice == 2:
        book_seat(manager)
    elif choice == 3:
        cancel_booking(manager)
    elif choice == 4:
        search_passenger(manager)
    elif choice == 5:
        fare_calculator()
    elif choice == 6:
        print("Thank you! Have a safe journey.")
        break
    actions[choice]()
