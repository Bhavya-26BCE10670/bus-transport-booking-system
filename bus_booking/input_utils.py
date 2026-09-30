def read_int(prompt, low=None, high=None):
    while True:
        try:
            value = int(input(prompt))
            if low is not None and value < low:
                print(f"Enter a number from {low} to {high}.")
                continue
            if high is not None and value > high:
                print(f"Enter a number from {low} to {high}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")
