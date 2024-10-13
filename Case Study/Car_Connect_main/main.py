from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from dao.reservation_service import ReservationService
from dao.admin_service import AdminService
from util.DBConnUtil import DBConnUtil
from util.DBPropertyUtil import DBPropertyUtil
from dao.authentication_service import AuthenticationService
from exception.exceptions import AuthenticationException
from dao.report_generator import ReportGenerator
from datetime import datetime, timedelta
from decimal import Decimal
from exception.exceptions import *
# from dao.admin_service import check_admin_id



def display_menu(menu_name, menu_options):
    print(f"{menu_name}:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    print("0. Exit")
def display_main_menu():
    menu_options = {
        '1': 'Customer Service',
        '2': 'Vehicle Service',
        '3': 'Reservation Service',
        '4': 'Admin Service',
        '5': 'Authentication Service',
        '6': 'Report Generation',

    }
    display_menu("Main Menu", menu_options)


def display_customer_menu():
    menu_options = {
        '1': 'Get Customer by ID',
        '2': 'Get Customer by Username',
        '3': 'Register a new Customer',
        '4': 'Update Customer information',
        '5': 'Delete a Customer',

    }
    display_menu("Customer Service", menu_options)


def display_vehicle_menu():
    menu_options = {
        '1': 'Get Vehicle by ID',
        '2': 'Get Available Vehicles',
        '3': 'Add Vehicle',
        '4': 'Update Vehicle',
        '5': 'Remove Vehicle',

    }
    display_menu("Vehicle Service", menu_options)


def display_reservation_menu():
    menu_options = {
        '1': 'Get Reservation by ID',
        '2': 'Get Reservation by CustomerId',
        '3': 'Create Reservation',
        '4': 'Update Reservation',
        '5': 'Cancel Reservation',

    }
    display_menu("Reservation Service", menu_options)


def display_admin_menu():
    menu_options = {
        '1': 'Get Admin by ID',
        '2': 'Get Admin by Username',
        '3': 'Register Admin',
        '4': 'Update Admin',
        '5': 'Delete Admin',

    }
    display_menu("Admin Service", menu_options)


def display_authentication_menu():
    menu_options = {
        '1': 'Authenticate Customer',
        '2': 'Authenticate Admin'
    }
    display_menu("Authentication Service", menu_options)


def display_reportgeneration_menu():
    menu_options = {
        '1': 'Generate Reservation Report',
        '2': 'Generate Vehicle Report'
    }
    display_menu("Report Generation", menu_options)


def main():
    connection_string = DBPropertyUtil.get_connection_string()
    db_conn_util = DBConnUtil()
    customer_service = CustomerService(db_conn_util, connection_string)
    vehicle_service = VehicleService(db_conn_util, connection_string)
    reservation_service = ReservationService(db_conn_util, connection_string)
    admin_service = AdminService(db_conn_util, connection_string)

    while True:
        display_main_menu()
        main_choice = input("Enter your choice (0-6): ")

        if main_choice == '0':
            print("Thankyou for using the Car Connect System.")
            break
        elif main_choice == '1':
            while True:
                display_customer_menu()
                customer_choice = input("Enter your choice (0-5): ")

                if customer_choice == '0':
                    break
                elif customer_choice == '1':
                    try:
                        customer_id = int(input("Enter customer ID to get: "))
                        customer_data = customer_service.GetCustomerById(customer_id)
                        
                        if customer_data:
                            print("\nCustomer Data:", customer_data)
                            
                    except CustomerNotFoundException as e:
                        print(str(e))  # Print the error message if the customer is not found
                    except ValueError:
                        print("Invalid input. Please enter a valid customer ID.")
                elif customer_choice == '2':
                    try:
                        username = input("Enter username to get customer data: ")
                        customer_data = customer_service.GetCustomerByUsername(username)
                        
                        if customer_data:
                            print("\nCustomer Data:", customer_data)
                            
                    except CustomerNotFoundException as e:
                        print(str(e)) 
                elif customer_choice == '3':
                    customer_data = {
                        'first_name': input("Enter first name: "),
                        'last_name': input("Enter last name: "),
                        'email': input("Enter email: "),
                        'phone_number': input("Enter phone number: "),
                        'address': input("Enter address: "),
                        'username': input("Enter username: "),
                        'password': input("Enter password: "),
                        'registration_date': input("Enter registration date (YYYY-MM-DD): ")
                    }
                    customer_service.RegisterCustomer(customer_data)
                elif customer_choice == '4':
                    try:
                        customer_id = int(input("Enter customer ID to update: "))
                        customer_data = customer_service.GetCustomerById(customer_id)
                        
                        if customer_data:
                            customer_data_to_update = {
                                'customer_id': customer_id,
                                'first_name': input("Enter updated first name: "),
                                'last_name': input("Enter updated last name: "),
                                'email': input("Enter updated email: "),
                                'phone_number': input("Enter updated phone number: "),
                                'address': input("Enter updated address: "),
                                'username': input("Enter updated username: "),
                                'password': input("Enter updated password: "),
                                'registration_date': input("Enter updated registration date (YYYY-MM-DD): ")
                            }
                            customer_service.UpdateCustomer(customer_data_to_update)
                            
                    except CustomerNotFoundException as e:
                        print(str(e))  # Print the error message if the customer is not found
                    except ValueError:
                        print("Invalid input. Please enter a valid customer ID.")
                    
                elif customer_choice == '5':
                    try:
                        customer_id = int(input("Enter customer ID to delete: "))
                        customer_data = customer_service.GetCustomerById(customer_id)
                        if customer_data:
                            customer_service.DeleteCustomer(customer_id)
                    
                    except CustomerNotFoundException as e:
                        print(str(e))  # Print the error message if the customer is not found
                    except ValueError:
                        print("Invalid input. Please enter a valid customer ID.")
                    
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '2':
            while True:
                display_vehicle_menu()
                vehicle_choice = input("Enter your choice (0-5): ")
                if vehicle_choice == '0':
                    break
                elif vehicle_choice == '1':
                    try:
                        vehicle_id_to_get = int(input("Enter vehicle ID to get: "))
                        vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)

                        if vehicle_data_to_get:
                            print("\nVehicle Data:", vehicle_data_to_get)
                            
                    except VehicleNotFoundException as e:
                        print(str(e))  # Print the error message if the vehicle is not found

                elif vehicle_choice == '2':
                    available_vehicles = vehicle_service.GetAvailableVehicles()

                    if available_vehicles:
                        print("\nAvailable Vehicles:")
                        for vehicle in available_vehicles:
                            print(vehicle)
                    else:
                        print("No available vehicles.")

                elif vehicle_choice == '3':
                    new_vehicle_data = {
                        'model': input("Enter model: "),
                        'make': input("Enter make: "),
                        'year': int(input("Enter year: ")),
                        'color': input("Enter color: "),
                        'registration_number': input("Enter registration number: "),
                        'availability': True,
                        'daily_rate': float(input("Enter daily rate: "))
                    }
                    vehicle_service.AddVehicle(new_vehicle_data)

                elif vehicle_choice == '4':
                    try:
                        vehicle_id_to_get = int(input("Enter vehicle ID to update: "))
                        vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)
                        if vehicle_data_to_get:
                            updated_vehicle_data = {
                                'vehicle_id':vehicle_id_to_get,
                                'model': input("Enter updated model: "),
                                'make': input("Enter updated make: "),
                                'year': int(input("Enter updated year: ")),
                                'color': input("Enter updated color: "),
                                'registration_number': input("Enter updated registration number: "),
                                'availability': True,
                                'daily_rate': float(input("Enter updated daily rate: "))
                            }
                            vehicle_service.UpdateVehicle(updated_vehicle_data)
                    except VehicleNotFoundException as e:
                        print(str(e))
                
                elif vehicle_choice == '5':
                    try:
                        vehicle_id_to_get = int(input("Enter vehicle ID to delete: "))
                        vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)
                        if vehicle_data_to_get:
                            vehicle_service.RemoveVehicle(vehicle_id_to_get)
                    
                    except VehicleNotFoundException as e:
                        print(str(e))
                    except ValueError:
                        print("Invalid input. Please enter a valid Vehicle ID.")

                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '3':
            while True:
                display_reservation_menu()
                reservation_choice = input("Enter your choice (0-5): ")
                if reservation_choice == '0':
                    break
                elif reservation_choice == '1':
                    try:
                        reservation_id_to_get = int(input("Enter reservation ID to get: "))
                        reservation_data_to_get = reservation_service.GetReservationById(reservation_id_to_get)

                        if reservation_data_to_get:
                            print("\nReservation Data:", reservation_data_to_get)
                    
                    except ReservationNotFoundException as e:
                        print(str(e)) 
                

                elif reservation_choice == '2':
                    try:
                        customer_id_to_get_reservations = int(input("Enter customer ID to get reservations: "))
                        reservations_data_by_customer = reservation_service.GetReservationsByCustomerId(
                            customer_id_to_get_reservations)

                        if reservations_data_by_customer:
                            print("\nReservations Data:")
                            for reservation in reservations_data_by_customer:
                                print(reservation)
                    except ReservationNotFoundException as e:
                        print(str(e)) 

                elif reservation_choice == '3':
                    try:
                        customer_id = int(input("Enter customer ID: "))
                        customer_data = customer_service.GetCustomerById(customer_id)
                        vehicle_id_to_get = int(input("Enter vehicle ID: "))
                        vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)
                        
                        if customer_data and vehicle_id_to_get:
                            reservation_data_to_create = {
                                'customer_id': customer_id,
                                'vehicle_id': vehicle_id_to_get,
                                'start_date': datetime.now(),
                                'end_date': datetime.now() + timedelta(
                                    days=int(input("Enter reservation duration (in days): "))),
                                'total_cost': Decimal(input("Enter total cost: ")),
                                'status': input("Enter reservation status: ")
                            }
                            reservation_service.CreateReservation(reservation_data_to_create)
                    except CustomerNotFoundException as e:
                        print(str(e))
                    except VehicleNotFoundException as e:
                        print(str(e))

                elif reservation_choice == '4':
                    try:
                        reservation_id_to_get = int(input("Enter reservation ID update: "))
                        reservation_data_to_get = reservation_service.GetReservationById(reservation_id_to_get)

                        customer_id = int(input("Enter customer ID: "))
                        customer_data = customer_service.GetCustomerById(customer_id)
                        vehicle_id_to_get = int(input("Enter vehicle ID: "))
                        vehicle_data_to_get = vehicle_service.GetVehicleById(vehicle_id_to_get)
                        
                        if customer_data and vehicle_id_to_get:
                            if reservation_data_to_get:
                                updated_reservation_data = {
                                    'reservation_id': reservation_id_to_get,
                                    'customer_id': customer_id,
                                    'vehicle_id': vehicle_id_to_get,
                                    'start_date': datetime.now(),
                                    'end_date': datetime.now() + timedelta(
                                        days=int(input("Enter updated reservation duration (in days): "))),
                                    'total_cost': Decimal(input("Enter updated total cost: ")),
                                    'status': input("Enter updated reservation status: ")
                                }
                                reservation_service.UpdateReservation(updated_reservation_data)
                    except ReservationNotFoundException as e:
                        print(str(e)) 
                    except CustomerNotFoundException as e:
                        print(str(e))
                    except VehicleNotFoundException as e:
                        print(str(e))

                elif reservation_choice == '5':
                    try:
                        reservation_id_to_get = int(input("Enter reservation ID to cancle: "))
                        reservation_data_to_get = reservation_service.GetReservationById(reservation_id_to_get)
                        if reservation_data_to_get:
                            reservation_service.CancelReservation(reservation_id_to_get)
                    except ReservationNotFoundException as e:
                        print(str(e))
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '4':
            while True:
                display_admin_menu()
                admin_choice = input("Enter your choice (0-5): ")
                if admin_choice == '0':
                    break
                if admin_choice == '1':
                    try:
                        admin_id_to_get = int(input("Enter admin ID to get: "))
                        admin_data_to_get = admin_service.GetAdminById(admin_id_to_get)

                        if admin_data_to_get:
                            print("\nAdmin Data:", admin_data_to_get)
                    
                    except AdminNotFoundException as e:
                        print(str(e)) 

                elif admin_choice == '2':
                    try:
                        admin_username_to_get = input("Enter admin username to get: ")
                        admin_data_by_username = admin_service.GetAdminByUsername(admin_username_to_get)

                        if admin_data_by_username:
                            print("\nAdmin Data:", admin_data_by_username)
                    
                    except AdminNotFoundException as e:
                        print(str(e)) 
                    
                    

                elif admin_choice == '3':
                    admin_data_to_register = {
                        'first_name': input("Enter first name: "),
                        'last_name': input("Enter last name: "),
                        'email': input("Enter email: "),
                        'phone_number': input("Enter phone number: "),
                        'username': input("Enter username: "),
                        'password': input("Enter password: "),
                        'role': input("Enter role: "),
                        'join_date': input("Enter join date (YYYY-MM-DD): ")
                    }
                    admin_service.RegisterAdmin(admin_data_to_register)

                elif admin_choice == '4':
                    try:
                        admin_id_to_get = int(input("Enter admin ID to update: "))
                        admin_data_to_get = admin_service.GetAdminById(admin_id_to_get)

                        if admin_data_to_get:
                            admin_data_to_update = {
                                'admin_id': admin_id_to_get,
                                'first_name': input("Enter updated first name: "),
                                'last_name': input("Enter updated last name: "),
                                'email': input("Enter updated email: "),
                                'phone_number': input("Enter updated phone number: "),
                                'username': input("Enter updated username: "),
                                'password': input("Enter updated password: "),
                            }
                            admin_service.UpdateAdmin(admin_data_to_update)
                            # print("Admin updated successfully.")
                    except AdminNotFoundException as e:
                        print(str(e)) 

                    

                elif admin_choice == '5':
                    try:
                        admin_id_to_get = int(input("Enter admin ID to update: "))
                        admin_data_to_get = admin_service.GetAdminById(admin_id_to_get)

                        if admin_data_to_get:
                            admin_service.DeleteAdmin(admin_id_to_get)
                    except AdminNotFoundException as e:
                        print(str(e))
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '5':
            while True:
                display_authentication_menu()
                auth_choice = input("Enter your choice (0-2): ")
                if auth_choice == '0':
                    break
                elif auth_choice == '1':
                    username = input("Enter customer username: ")
                    password = input("Enter customer password: ")

                    try:
                        customer = AuthenticationService.authenticate_customer(username, password, connection_string)
                        print("Customer authenticated:", customer)

                    except AuthenticationException as e:
                        print(f"Authentication failed: {str(e)}")
                    except CustomerNotFoundException as e:
                        print(f"Authentication failed: {str(e)}")

                elif auth_choice == '2':
                    admin_username = input("Enter admin username: ")
                    admin_password = input("Enter admin password: ")

                    try:
                        admin = AuthenticationService.authenticate_admin(admin_username, admin_password,
                                                                         connection_string)
                        print("Admin authenticated:", admin)

                    except AuthenticationException as e:
                        print(f"Authentication failed: {str(e)}")
                    except AdminNotFoundException as e:
                        print(f"Authentication failed: {str(e)}")
                else:
                    print("Invalid choice. Please enter a valid option.")
        elif main_choice == '6':
            while True:
                display_reportgeneration_menu()
                report_choice = input("Enter your choice (0-2): ")
                if report_choice == '0':
                    break
                elif report_choice == '1':
                    reservation_service = ReservationService(db_conn_util, connection_string)
                    reservation_data = reservation_service.GetReservationsList()
                    ReportGenerator.generate_reservation_report(reservation_data)
                    print("Reservation Report generated successfully.")

                elif report_choice == '2':
                    vehicle_service = VehicleService(db_conn_util, connection_string)
                    vehicle_data = vehicle_service.GetAvailableVehicles()
                    ReportGenerator.generate_vehicle_report(vehicle_data)
                    print("Vehicle Report generated successfully.")
                else:
                    print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()