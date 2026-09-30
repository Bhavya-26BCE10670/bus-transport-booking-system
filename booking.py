
    #Stores bookings and keeps track of occupied seats.

def __init__(self, routes, total_seats):
    self.routes = routes
    self.total_seats = total_seats
    self.bookings = {}
    self.seats = {route_id: {} for route_id in routes}
    self.next_ticket = 1001

def available_seats(self, route_id):
    x=self.total_seats - len(self.seats[route_id])
    return x

def book(self, route_id, seat, name, age, phone, fare):
    if route_id not in self.routes:
        return False, "Invalid route."
    if seat < 1 or seat > self.total_seats:
        return False, "Invalid seat number."
    if seat in self.seats[route_id]:
        return False, "That seat is already booked."

    ticket_id = self.next_ticket
    self.next_ticket += 1

    self.bookings[ticket_id] = {"name": name,"age": age,"phone": phone,"route": route_id,"seat": seat,"fare": fare}
    ticket_id=seats[route_id][seat] 
    return True, ticket_id

def cancel(self, ticket_id):
    booking = self.bookings.get(ticket_id)
    if booking is None:
        return False, None

    refund = round(booking["fare"] * 0.90, 2)
    del self.seats[booking["route"]][booking["seat"]]
    del self.bookings[ticket_id]
    return True , refund

def search(self, key):
    key = key.strip().lower()
    l= [
        (ticket_id, booking)
        for ticket_id, booking in self.bookings.items()
        if key in booking["name"].lower() or key in str(booking["phone"])
    ]
    return l