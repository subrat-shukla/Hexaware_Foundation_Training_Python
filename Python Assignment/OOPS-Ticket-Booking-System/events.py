import decimal
import enum

class event:
    def __init__(self,event_name,event_date,event_time,venue_name,
                 total_seats,available_seats,
                 ticket_price: decimal,event_type: enum):
        self.event_name=event_name
        self.event_date=event_date
        self.event_time=event_time
        self.venue_name=venue_name
        self.total_seats=total_seats
        self.available_seats=available_seats
        self.ticket_price=ticket_price
        self.event_type=event_type

    # getters
    @property
    def get_event_name(self):
        return self.event_name

    @property
    def get_event_date(self):
        return self.event_date
    @property
    def get_event_time(self):
        return self.event_time

    @property
    def get_venue_name(self):
        return self.venue_name

    @property
    def get_total_seats(self):
        return self.total_seats

    @property
    def get_available_seats(self):
        return self.available_seats

    @property
    def get_ticket_price(self):
        return self.ticket_price

    @property
    def get_event_type(self):
        return self.event_type

    #setters
    @get_event_date.setter
    def set_event_name(self,event_name):
         self.event_name=event_name
    @ get_event_date.setter
    def set_event_date(self,event_date):
        self.event_date=event_date
    @get_event_time.setter
    def set_event_time(self,event_time):
        self.event_time=event_time
    @get_venue_name.setter
    def set_venue_name(self,venue_name):
        self.venue_name=venue_name
    @get_total_seats.setter
    def set_total_seats(self,total_seats):
        self.total_seats=total_seats
    @get_available_seats.setter
    def set_available_seats(self,available_seats):
        self.available_seats=available_seats
    @get_ticket_price.setter
    def set_ticket_price(self,ticket_price):
        self.ticket_price=ticket_price
    @get_event_type.setter
    def set_event_type(self,event_type):
        self.event_type=event_type

    def print_event_info(self):
        print("Event name: ",self.event_name)
        print("Event_date: ", self.event_date)
        print("Event_time: ", self.event_time)
        print("Venue_name: ", self.venue_name)
        print("Total_seats: ", self.total_seats)
        print("Available_seats: ", self.available_seats)
        print("Ticket_price: ", self.ticket_price)
        print("Event_type: ", self.event_type)

    def totalrevenue(self):
        tickets_sold=self.total_seats-self.available_Seats
        return tickets_sold*self.ticket_price

    def totaltickets_sold(self):
        return self.total_seats-self.available_Seats

    def book_tickets(self,num_tickets):
        if num_tickets <=self.available_seats:
            self.available_seats-=num_tickets
            print(f"Booked{num_tickets}tickets. Available seats: {self.available_seats}")
        else:
            print("Not enough available seats for the requested number of tickets.")

    def cancel_tickets(self,num_tickets):
        self.available_seats+=num_tickets
        print(f"After canceling{num_tickets} available tickets are {self.available_seats}")

event1=event("Concert", "2024-5-15","18:30", "City Hall", 1000, 800, 50.0, "Concert")
#event1.set_event_name="concert"
print(event1.get_event_name)
print(event1.get_available_seats)
event1.book_tickets(5)
event1.cancel_tickets(2)

# task-5
from events import event
class movie(event):
    def __init__(self):
        self.genre=" "
        self.actorname=" "
        self.actressname=" "

    @property
    def getgenre(self):
        return self.genre
    @property
    def getactorname(self):
        return self.actorname
    @property
    def getactressname(self):
        return self.actressname

    @getgenre.setter
    def setgenre(self,genre):
        self.genre=genre
    @getactorname.setter
    def setactorname(self,actorname):
        self.actorname=actorname
    @getactressname.setter
    def setactressname(self,actressname):
        self.actressname=actressname

    def display_event_details(self):
        event1.print_event_info()
        print("genre: ",self.genre)

m=movie()
m.setgenre="horror"
m.setactorname="prince"
m.setactressname="nataile"
print("genre: ",m.getgenre)
print("actress name: ",m.getactressname)
print("actor name: ",m.getactorname)
m.display_event_details()

class concert(event):
    def __int__(self):
        self.artist=" "
        self.type=" "

    @property
    def getartist(self):
        return self.artist
    @getartist.setter
    def setartist(self,artist):
        self.artist=artist

    @property
    def gettype(self):
        return self.type

    @getartist.setter
    def settype(self, type):
        self.type = type

    def display_concert_details(self):
        event1.print_event_info()
        print("artist: ", self.artist)

'''con=concert()
con.setartist="akash"
print(con.getartist)
con.settype="classical"
print(con.gettype)
con.display_concert_details()'''

class sports(event):
    def __init__(self):
        self.sportname=" "
        self.teams=" "

    @property
    def getsportname(self):
        return self.sportname
    @property
    def getteams(self):
        return self.teams

    @getsportname.setter
    def setsportname(self,sportname):
        self.sportname=sportname
    @getteams.setter
    def setactorname(self,teams):
        self.teams=teams

    def display_sport_details(self):
        event1.print_event_info()
        print("genre: ",self.sportname)

'''sp=sports()
sp.setsportname="cricket"
print("sportsname: ",sp.getsportname)
sp.setteams="india vs pakistan"
print("teams: ",sp.getteams)
sp.display_sport_details()'''

class TicketBookingSystem:
    def __init__(self):
        self.events = []
    def create_event(self,event_name: str, date:str, time:str, total_seats: int,
                     ticket_price: float, event_type: str, venue_name:str):
        new_event = event(event_name, date, time, total_seats, ticket_price,
                          event_type, venue_name)
        self.events.append(new_event)
        return new_event

    def display_event_details(self, event):
        event.display_event_details()

    def book_tickets(self, event, num_tickets):
        if num_tickets <= event.availableSeats:
            event.availableSeats -= num_tickets
            total_cost = num_tickets * event.ticketPrice
            return total_cost
        else:
            print("Sorry, the event is sold out. Not enough available seats.")
            return 0

    def cancel_tickets(self, event, num_tickets):
        event.availableSeats += num_tickets
        print(f"{num_tickets} tickets canceled for the event.")

    def main(self):
        while True:
            print("\n1. Create Event\n2. Display Event Details\n"
                  "3. Book Tickets\n4. Cancel Tickets\n5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                event_name = input("Enter event name: ")
                date = input("Enter date: ")
                time = input("Enter time: ")
                total_seats = int(input("Enter total seats: "))
                ticket_price = float(input("Enter ticket price: "))
                event_type = input("Enter event type (movie, sport, concert): ")
                venue_name = input("Enter venue name: ")

                new_event = self.create_event(event_name, date, time, total_seats,
                                              ticket_price, event_type, venue_name)
                print(f"Event '{new_event.eventName}' created successfully!")

            elif choice == '2':
                event_index = int(input("Enter the index of the event to display details: "))
                if 0 <= event_index < len(self.events):
                    self.display_event_details(self.events[event_index])
                else:
                    print("Invalid event index.")

            elif choice == '3':
                event_index = int(input("Enter the index of the event to book tickets: "))
                if 0 <= event_index < len(self.events):
                    num_tickets = int(input("Enter the number of tickets to book: "))
                    total_cost = self.book_tickets(self.events[event_index], num_tickets)
                    if total_cost > 0:
                        print(f"Tickets booked successfully! Total Cost: ${total_cost}")
                else:
                    print("Invalid event index.")

            elif choice == '4':
                event_index = int(input("Enter the index of the event to cancel tickets: "))
                if 0 <= event_index < len(self.events):
                    num_tickets = int(input("Enter the number of tickets to cancel: "))
                    self.cancel_tickets(self.events[event_index], num_tickets)
                else:
                    print("Invalid event index.")

            elif choice == '5':
                print("Exiting the Ticket Booking System.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

t1=TicketBookingSystem
t1.main(self=2)


#### task-8
