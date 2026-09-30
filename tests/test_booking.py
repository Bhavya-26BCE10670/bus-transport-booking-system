import unittest
from bus_booking.booking import BookingManager
from bus_booking.routes import ROUTES
from bus_booking.fare import calculate_fare

class TestBusBooking(unittest.TestCase):
    def setUp(self):
        self.manager = BookingManager(ROUTES, 40)

    def test_normal_booking(self):
        ok, ticket = self.manager.book(1, 5, "Aman", 20, "9999999999", calculate_fare(1, 20))
        self.assertTrue(ok)
        self.assertEqual(ticket, 1001)
        self.assertEqual(self.manager.available_seats(1), 39)

    def test_duplicate_seat(self):
        fare = calculate_fare(1, 20)
        self.manager.book(1, 5, "Aman", 20, "999", fare)
        ok, message = self.manager.book(1, 5, "Ravi", 21, "888", fare)
        self.assertFalse(ok)
        self.assertEqual(message, "That seat is already booked.")

    def test_cancellation_refund(self):
        fare = calculate_fare(1, 20)
        _, ticket = self.manager.book(1, 5, "Aman", 20, "999", fare)
        ok, refund = self.manager.cancel(ticket)
        self.assertTrue(ok)
        self.assertEqual(refund, round(fare * 0.90, 2))
        self.assertEqual(self.manager.available_seats(1), 40)

    def test_fare_discount(self):
        self.assertEqual(calculate_fare(1, 10), 81.25)
        self.assertEqual(calculate_fare(1, 60), 130.0)

if __name__ == "__main__":
    unittest.main()
