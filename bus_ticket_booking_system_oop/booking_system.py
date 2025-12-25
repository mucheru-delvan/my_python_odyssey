import json
from pathlib import Path 

BASE_DIR = Path(__file__).parent

class BookingSystem:
    def __init__(self,filename="bookings.json"):
        self.filename = BASE_DIR/filename
        self.tickets = self.load_tickets()

    def load_tickets(self):
        with open(self.filename,"r") as f:
            return json.load(f)
    
    def save_tickets(self):
        with open(self.filename,"w") as f:
            json.dump(self.tickets,f,indent=4)


    def view_tickets(self):
        if not self.tickets:
            print("No tickets added available!")
            return
        
        print("\nTickets Added\n")
        for i,ticket in enumerate(self.tickets,start=1):
            print(f"{i}.{ticket}")


    def add_tickets(self,ticket):
       for existing in self.tickets:
           if existing.ticket_id == ticket.ticket_id:
               return f"Ticket {ticket.ticket_id} already exists."
       
       self.tickets.append(ticket)
       self.save_tickets() 
       return f" Ticket {ticket.ticket_id} added successfully."
    

    def remove_ticket(self,ticket_num):
        for existing in self.tickets:
            if existing.ticket_id == ticket_num:
                self.tickets.remove(ticket_num)
                self.save_tickets()
                return f"{ticket_num} was removed."
            
        return f"{ticket_num} was not found."
    
            





        