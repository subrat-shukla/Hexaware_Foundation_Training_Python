#from events import event
import pyodbc
from dbutil import DBConnection

con = DBConnection.getConnection()
cur=con.cursor()

class EventNotFoundException(Exception):
    pass
class InvalidBookingIDException(Exception):
    pass


class TicketBookingSystem1():

    def book_tickets_menu(self):
        try:
            eventname = input("Enter the event name: ")
            # Check if the event exists
            query1="select * from event where event_name=%s"
            cur.execute(query1,(eventname,))
            event=cur.fetchone()

            if not event:
                raise EventNotFoundException(f"Event '{eventname}' not found in the menu.")

        except EventNotFoundException as e:
            print(f"Error: {e}")

    def booking_details_menu(self):
        try:
            booking_id = input("Enter the booking ID: ")
            query1 = "select * from booking where booking_id=%s"
            cur.execute(query1,(booking_id,))
            booking = cur.fetchone()

            if not booking:
                raise InvalidBookingIDException(f"Invalid booking ID: {booking_id}")

        except InvalidBookingIDException as e:
            print(f"Error: {e}")

    def event_exists(self, event_name):
        pass

    def is_valid_booking_id(self, booking_id):
        pass

if __name__ == "__main__":
    ticket = TicketBookingSystem1()
    ticket.book_tickets_menu()
    ticket.booking_details_menu()
