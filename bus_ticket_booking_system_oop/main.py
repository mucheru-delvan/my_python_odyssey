from bus import Bus
from ticket import Ticket
from booking_system import BookingSystem

bus1 = Bus("Volvo", "City A to City B", 20)
bus2 = Bus("Mercedes", "City C to City D", 30)
bus3 = Bus("Scania", "City E to City F", 25)

#print(bus1)
ticket1 = Ticket("P001","Levrone",bus1.model,"12")
ticket1_dict = ticket1.to_dict()
#print(ticket1_dict)
ticket2 = Ticket("P002","Ronnie",bus1.model,"14")
ticket2_dict = ticket2.to_dict()
#print(ticket2)

#bus1.display_layout()
#bus1.book_seat(12)
#bus1.display_layout()
booking1 = BookingSystem()
print(booking1.add_tickets(ticket1_dict))
print(booking1.add_tickets(ticket2_dict))
booking1.view_tickets()


