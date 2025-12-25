class Bus:
    def __init__(self, model, route, capacity):
        self.model = model
        self.route = route
        self.capacity = capacity
        self.booked_seats = set()

    def display_layout(self):
        print(f"Bus Model: {self.model}, Route: {self.route}")
        print("Seat Layout:")

        for seat_number in range(1, self.capacity + 1):
            status = "[✓]" if seat_number in self.booked_seats else "[]"
            print(status, end="")

        
            if seat_number % 4 == 2:
                print("  |  ", end="")


            if seat_number % 4 == 0:
                print()

        print()


    def book_seat(self, seat_number):

        if seat_number < 1 or seat_number > self.capacity:
            print("Invalid seat number.")
            return False
        
        if seat_number in self.booked_seats:
            print("Seat already booked.")
            return False
        
        self.booked_seats.add(seat_number)
        print(f"Seat {seat_number} successfully booked.")
        return True 
    
    def cancel_booking(self, seat_number):
        if seat_number in self.booked_seats:
            self.booked_seats.remove(seat_number)
            print(f"Booking for seat {seat_number} cancelled.")
            return True
        else:
            print("Seat is not booked.")
            return False
        
    def available_seats(self):
        return self.capacity - len(self.booked_seats)
    
    def __str__(self):
        return f"Bus Model: {self.model}, Route: {self.route}, Capacity: {self.capacity}, Available Seats: {self.available_seats()}"
