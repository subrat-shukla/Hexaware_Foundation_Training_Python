
from dao.IReservationService import IReservationService
from exception.exceptions import ReservationNotFoundException
from decimal import Decimal
from exception.exceptions import ReservationException


class ReservationService(IReservationService):
    def __init__(self, db_conn_util, connection_string):
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string

    def GetReservationById(self, reservation_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation WHERE ReservationID = ?", (reservation_id,))
            reservation_data = cursor.fetchone()

            if reservation_data:
                return reservation_data
            else:
                raise ReservationNotFoundException(f"Reservation with ID {reservation_id} not found.")
            
        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetReservationsByCustomerId(self, customer_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation WHERE CustomerID = ?", (customer_id,))
            reservations_data = cursor.fetchall()

            if reservations_data:
                return reservations_data
            else:
                raise ReservationNotFoundException(f"No reservations found for Customer ID {customer_id}.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def CreateReservation(self, reservationData,):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO Reservation (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                reservationData['customer_id'],
                reservationData['vehicle_id'],
                reservationData['start_date'],
                reservationData['end_date'],
                Decimal(reservationData['total_cost']),
                reservationData['status']
            ))

            connection.commit()
            print("Reservation created successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def UpdateReservation(self, reservation_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute(""" 
                UPDATE Reservation 
                SET CustomerID = ?, 
                    VehicleID = ?, 
                    StartDate = ?, 
                    EndDate = ?, 
                    TotalCost = ?, 
                    Status = ? 
                WHERE ReservationID = ?
            """, (
                reservation_data['customer_id'],
                reservation_data['vehicle_id'],
                reservation_data['start_date'],
                reservation_data['end_date'],
                reservation_data['total_cost'],
                reservation_data['status'],
                reservation_data['reservation_id']
            ))

            # Check if any rows were affected
            if cursor.rowcount == 0:
                print(f"No reservation found with ID {reservation_data['reservation_id']} to update.")
            else:
                connection.commit()
                print("Reservation updated successfully.")

        except Exception as e:
            print(f"An error occurred while updating the reservation: {str(e)}")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()


    def CancelReservation(self, reservation_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE Reservation
                SET Status = 'Cancelled'
                WHERE ReservationID = ?
            """, (reservation_id,))

            connection.commit()
            print(f"Reservation with ID {reservation_id} has been cancelled.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetReservationsList(self):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Reservation")
            reservations_data = cursor.fetchall()

            if reservations_data:
                return reservations_data
            else:
                raise ReservationNotFoundException("No reservations found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()
