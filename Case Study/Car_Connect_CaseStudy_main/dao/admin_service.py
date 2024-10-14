from dao.IAdminService import IAdminService
from exception.exceptions import AdminNotFoundException


class AdminService(IAdminService):
    def __init__(self, db_conn_util, connection_string):
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string

    def GetAdminById(self, admin_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Admin WHERE AdminID = ?", (admin_id,))
            admin_data = cursor.fetchone()

            if admin_data:
                return admin_data
            else:
                raise AdminNotFoundException(f"Admin with ID {admin_id} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def GetAdminByUsername(self, username):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("SELECT AdminID, Password FROM Admin WHERE Username = ?", (username,))
            admin_data1 = cursor.fetchone()

            if admin_data1:
                admin_dict = {
                    'AdminID': admin_data1[0],
                    'Password': admin_data1[1]
                }
                return admin_dict
            else:
                raise AdminNotFoundException(f"Customer with FirstName {username} not found.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def RegisterAdmin(self, admin_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                   INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?)
               """, (
                admin_data['first_name'],
                admin_data['last_name'],
                admin_data['email'],
                admin_data['phone_number'],
                admin_data['username'],
                admin_data['password'],
                admin_data['role'],
                admin_data['join_date']
            ))

            connection.commit()
            print("Admin registered successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def UpdateAdmin(self, admin_data):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("""
                UPDATE Admin
                SET FirstName = ?, LastName = ?, Email = ?, PhoneNumber = ?, Password = ?
                WHERE AdminID = ?
            """, (
                admin_data['first_name'],
                admin_data['last_name'],
                admin_data['email'],
                admin_data['phone_number'],
                admin_data['password'],
                admin_data['admin_id']
            ))

            connection.commit()
            print("Admin updated successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()

    def DeleteAdmin(self, admin_id):
        try:
            connection = self._db_conn_util.get_connection(self._connection_string)
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Admin WHERE AdminID = ?", (admin_id,))

            connection.commit()
            print("Admin deleted successfully.")

        finally:
            if 'connection' in locals() or 'connection' in globals():
                connection.close()