from dao.IVehicleService import IVehicleService
from exception.exceptions import VehicleNotFoundException


class VehicleService(IVehicleService):
    def __init__(self, db_conn_util, connection_string):
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string

    def GetVehicleById(self, vehicle_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))
            vehicle_data = cursor.fetchone()

            if vehicle_data:
                return vehicle_data
            else:
                raise VehicleNotFoundException(f"Vehicle with ID {vehicle_id} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetAvailableVehicles(self):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Vehicle WHERE Availability>0")
            available_vehicles = cursor.fetchall()

            return available_vehicles

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def AddVehicle(self, vehicle_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                vehicle_data['model'],
                vehicle_data['make'],
                vehicle_data['year'],
                vehicle_data['color'],
                vehicle_data['registration_number'],
                vehicle_data['availability'],
                vehicle_data['daily_rate']
            ))

            connection.commit()
            print("Vehicle added successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def UpdateVehicle(self, vehicle_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()
            cursor.execute("""
                UPDATE Vehicle
                SET Model = ?, Make = ?, Year = ?, Color = ?,
                    RegistrationNumber = ?, Availability = ?, DailyRate = ?
                WHERE VehicleID = ?
            """, (
                vehicle_data['model'],
                vehicle_data['make'],
                vehicle_data['year'],
                vehicle_data['color'],
                vehicle_data['registration_number'],
                vehicle_data['availability'],
                vehicle_data['daily_rate'],
                vehicle_data['vehicle_id']
            ))

            connection.commit()
            print("Vehicle updated successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def RemoveVehicle(self, vehicle_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Vehicle WHERE VehicleID = ?", (vehicle_id,))

            connection.commit()
            print("Vehicle removed successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()