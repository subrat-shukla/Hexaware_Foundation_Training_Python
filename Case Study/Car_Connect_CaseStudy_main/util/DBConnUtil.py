import pyodbc


class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-MKS6P3G;'
                      'Database=CarConnectSystem;'
                      'Trusted_Connection=yes;')

            return connection
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")
            return None