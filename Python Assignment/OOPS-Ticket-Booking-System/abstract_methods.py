from abc import ABC, abstractmethod

class IBookingSystemRepository:
    def create_event(self):
        pass
    def get_Event_Details(self):
        pass
    def get_available_tickets(self):
        pass
    def book_tickets(self,num_tickets):
        pass
    def cancel_tickets(self):
        pass

class BookingSystemRepositoryImpl(IBookingSystemRepository):
    def create_event(self):
        return True
    def get_Event_Details(self):
        return True
    def get_available_tickets(self):
        return True
    def book_tickets(self,num_tickets):
        return True
    def cancel_tickets(self):
        return True
