from exception.exceptions import AuthenticationException, CustomerNotFoundException, AdminNotFoundException
from dao.customer_service import CustomerService
from dao.admin_service import AdminService
from util.DBConnUtil import DBConnUtil

class AuthenticationService:
    def __init__(self, customer_service, db_conn_util, connection_string):
        self._customer_service = customer_service
        self._db_conn_util = db_conn_util
        self._connection_string = connection_string
    
    @staticmethod
    def authenticate_customer(username, password,connection_string):
        try:
            # Initialize CustomerService with DB connection
            customer_service = CustomerService(DBConnUtil(),connection_string)

            # Check if customer exists in the database
            customer_data = customer_service.GetCustomerByUsername(username)

            if not customer_data:
                raise CustomerNotFoundException(f"Customer with username '{username}' not found.")

            # Validate password
            if customer_data['Password'] == password:
                print("Authentication successful.")
                return customer_data
            else:
                raise AuthenticationException("Incorrect customer password.")

        except CustomerNotFoundException as e:
            print(f"Error during customer authentication: {str(e)}")
            raise

        except AuthenticationException as e:
            print(f"Error during customer authentication: {str(e)}")
            raise

    @staticmethod
    def authenticate_admin(username, password, connection_string):
        try:
            # Initialize AdminService with DB connection
            admin_service = AdminService(DBConnUtil(),connection_string)

            # Check if admin exists in the database
            admin_data = admin_service.GetAdminByUsername(username)

            if not admin_data:
                raise AuthenticationException(f"Admin with username '{username}' not found.")

            # Validate password
            if admin_data['Password'] == password:
                print("Authentication successful.")
                return admin_data
            else:
                raise AuthenticationException("Incorrect admin password.")

        except AdminNotFoundException as e:
            print(f"Error during Admin authentication: {str(e)}")
            raise
        except AuthenticationException as e:
            print(f"Error during admin authentication: {str(e)}")
            raise
