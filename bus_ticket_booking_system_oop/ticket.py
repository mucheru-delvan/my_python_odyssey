class Ticket:
    def __init__(self, ticket_id, passenger_name, model, seat_number):
        self.ticket_id = ticket_id
        self.passenger_name = passenger_name
        self.model = model
        self.seat_number = seat_number
        

    def __str__(self):
        return (f"Ticket ID: {self.ticket_id}\n"
                f"Passenger Name: {self.passenger_name}\n"
                f"Bus Model: {self.model}\n"
                f"Seat Number: {self.seat_number}\n")
                

    
    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "passenger_name": self.passenger_name,
            "bus_model": self.model,
            "seat_number": self.seat_number
        }


