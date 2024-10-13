class bookings:
    def __int__(self,event_id,num_tickets,total_cost,booking_date):
        self.event_id=event_id
        self.num_tickets=num_tickets
        self.total_cost=total_cost
        self.booking_date=booking_date

    @property
    def getevent_id(self):
        return self.event_id
    @property
    def getnum_tickets(self):
        return self.num_tickets
    @property
    def total_cost(self):
        return self.total_cost
    @property
    def booking_date(self):
        return self.booking_date

    @getevent_id.setter
    def setevent_id(self,event_id):
        self.event_id=event_id
    @getnum_tickets.setter
    def setnum_tickets(self,num_tickets):
        self.num_tickets=num_tickets

    @total_cost.setter
    def settotal_cost(self,total_cost):
        self.total_cost=total_cost

    @booking_date.setter
    def setbooking_date(self,booking_date):
        self.booking_date=booking_date