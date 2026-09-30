# Bus / Transport Booking System

A simple command-line Python project for managing bus routes and passenger bookings. The project was built as a VITyarthi course project to practice Python functions, dictionaries, classes, input validation, modular programming, and basic testing.

## Features

1. Display available routes and remaining seats.
2. Book a seat for a passenger.
3. Cancel a booking and calculate the refund.
4. Search passengers by name or ticket ID.
5. Calculate fares using distance, route rate, and age-based discounts.
6. Validate common user input errors.
7. Run unit tests for important booking and fare operations.

## Technologies Used

- Python 3
- Python standard library
- `unittest`
- Git and GitHub

No external Python packages are required.

## Project Structure

```text
BusBookingSystem/
├── bus_booking/
│   ├── __init__.py
│   ├── app.py
│   ├── booking.py
│   ├── display.py
│   ├── fare.py
│   ├── input_utils.py
│   └── routes.py
├── tests/
│   └── test_booking.py
├── main.py
├── statement.md
└── README.md
```

## Requirements

Install Python 3.9 or newer. Check it with:

```bash
python --version
```

On some systems the command may be:

```bash
python3 --version
```

## How to Run

1. Download or clone this repository.
2. Open a terminal in the project root folder.
3. Run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

The program opens a text menu. Enter the number for the operation you want.

## How to Test

From the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover normal booking, duplicate-seat handling, cancellation/refund, and fare discounts.

## Fare Logic

The basic fare is:

```text
Base fare + distance × route rate
```

Age discounts:
- Below 12 years: 50% discount
- 12–59 years: no age discount
- 60 years and above: 20% discount

Cancellation returns 90% of the ticket fare, so a 10% cancellation charge is applied.

## Important Note

The current version stores booking data in memory. Closing the program clears the bookings. A future version could add file or database storage.

## Author

Student Project — VITyarthi
