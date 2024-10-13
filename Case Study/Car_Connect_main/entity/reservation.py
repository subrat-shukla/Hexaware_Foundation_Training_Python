from datetime import datetime


class Reservation:
    def __init__(self, reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status):
        self._reservation_id = reservation_id
        self._customer_id = customer_id
        self._vehicle_id = vehicle_id
        self._start_date = start_date
        self._end_date = end_date
        self._total_cost = total_cost
        self._status = status

    def get_reservation_id(self):
        return self._reservation_id

    def get_customer_id(self):
        return self._customer_id

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_total_cost(self):
        return self._total_cost

    def get_status(self):
        return self._status

    def set_reservation_id(self, reservation_id):
        if isinstance(reservation_id, int) and reservation_id > 0:
            self._reservation_id = reservation_id
        else:
            print("Invalid reservation_id. It should be a positive integer.")

    def set_customer_id(self, customer_id):
        if isinstance(customer_id, int) and customer_id > 0:
            self._customer_id = customer_id
        else:
            print("Invalid customer_id. It should be a positive integer.")

    def set_vehicle_id(self, vehicle_id):
        if isinstance(vehicle_id, int) and vehicle_id > 0:
            self._vehicle_id = vehicle_id
        else:
            print("Invalid vehicle_id. It should be a positive integer.")

    def set_start_date(self, start_date):
        if isinstance(start_date, str):
            self._start_date = start_date
        else:
            print("Invalid start_date. It should be a valid date format.")

    def set_end_date(self, end_date):
        if isinstance(end_date, str):
            self._end_date = end_date
        else:
            print("Invalid end_date. It should be a valid date format.")

    def set_total_cost(self, total_cost):
        if isinstance(total_cost, (int, float)) and total_cost >= 0:
            self._total_cost = total_cost
        else:
            print("Invalid total_cost. It should be a non-negative number.")

    def set_status(self, status):
        self._status = status

    def calculatetotalcost(self):
        start_date = datetime.strptime(self._start_date, "%Y-%m-%d")
        end_date = datetime.strptime(self._end_date, "%Y-%m-%d")
        days_rented = (end_date - start_date).days
        daily_rate = 50
        self._total_cost = days_rented * daily_rate

    @classmethod
    def create_from_input(cls):
        reservation_id = int(input("Enter ReservationID: "))
        customer_id = int(input("Enter CustomerID: "))
        vehicle_id = int(input("Enter VehicleID: "))
        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")
        total_cost = 0
        status = input("Enter Status: ")
        print("Reservation done successfully ")
        return cls(reservation_id, customer_id, vehicle_id, start_date, end_date, total_cost, status)


reservation_instance = Reservation.create_from_input()
reservation_instance.calculatetotalcost()
print("Total Cost:", reservation_instance._total_cost)