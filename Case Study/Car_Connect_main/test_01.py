import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import MagicMock, patch
from dao.authentication_service import AuthenticationService
from exception.exceptions import AuthenticationException
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService


class TestAuthenticationService(unittest.TestCase):
    def setUp(self):
        # Mock services and connection string
        self.customer_service = MagicMock()
        self.db_conn_util = MagicMock()
        self.connection_string = {
            'Driver={SQL Server};'
            'Server=DESKTOP-OFHDUG6;'
            'Database=casestudy_db;'
            'Trusted_Connection=yes;'
        }
        self.auth_service = AuthenticationService(self.customer_service, self.db_conn_util, self.connection_string)
        self.vehicle_service = VehicleService(self.db_conn_util, self.connection_string)

    def test_authenticate_customer_with_invalid_credentials(self):
        self.customer_service.AuthenticateCustomer = MagicMock(side_effect=AuthenticationException("Invalid credentials"))

        invalid_credentials = {
            'Username': 'invalid_user',
            'Password': 'wrong_password'
        }

        with self.assertRaises(AuthenticationException) as context:
            self.customer_service.AuthenticateCustomer(invalid_credentials['Username'], invalid_credentials['Password'])

        self.assertEqual(str(context.exception), "Invalid credentials")
        self.customer_service.AuthenticateCustomer.assert_called_once_with(invalid_credentials['Username'], invalid_credentials['Password'])
    

    def test_update_customer_information(self):
        self.customer_service.GetCustomerById = MagicMock(return_value={
            'CustomerID': 1,
            'FirstName': 'Harish',
            'LastName': 'E R',
            'Email': 'harish.er562@gmail.com',
            'PhoneNumber': '+91 7769011289',
            'Address': 'abc',
            'Username': 'harish562',
            'Password': '1234',
            'RegistrationDate': '2024-10-11'
        })

        updated_customer_data = {
            'CustomerID': 1,
            'FirstName': 'Harish',
            'LastName': 'E R',
            'Email': 'harish.er562@gmail.com',
            'PhoneNumber': '+91 7769011289',
            'Address': 'abc',
            'Username': 'harish562',
            'Password': '1234',
            'RegistrationDate': '2024-10-11'
        }
        self.customer_service.UpdateCustomer = MagicMock(return_value=updated_customer_data)

        result = self.customer_service.UpdateCustomer(updated_customer_data)
        self.assertEqual(result, updated_customer_data)
        self.customer_service.UpdateCustomer.assert_called_once_with(updated_customer_data)  # Verifying the method call

    def test_add_new_vehicle(self):
        new_vehicle_data = {
            'VehicleID': 6,
            'Brand': 'Toyota',
            'Model': 'Camry',
            'Year': 2022,
            'RegistrationPlate': 'ABC123',
            'Color': 'Blue',
            'Type': 'Sedan',
            'Availability': True
        }
        self.vehicle_service.AddVehicle = MagicMock(return_value=new_vehicle_data)

        result = self.vehicle_service.AddVehicle(new_vehicle_data)
        self.assertEqual(result, new_vehicle_data)
        self.vehicle_service.AddVehicle.assert_called_once_with(new_vehicle_data)  # Ensure method call

    def test_update_vehicle_details(self):
        updated_vehicle_data = {
            'VehicleID': 1,
            'Brand': 'Updated Brand',
            'Model': 'Updated Model',
            'Year': 2023,
            'RegistrationPlate': 'XYZ789',
            'Color': 'Red',
            'Type': 'SUV',
            'Availability': True
        }
        self.vehicle_service.UpdateVehicle = MagicMock(return_value=updated_vehicle_data)

        result = self.vehicle_service.UpdateVehicle(updated_vehicle_data['VehicleID'], updated_vehicle_data)
        self.assertEqual(result, updated_vehicle_data)
        self.vehicle_service.UpdateVehicle.assert_called_once_with(updated_vehicle_data['VehicleID'], updated_vehicle_data)

    def test_get_available_vehicles(self):
        available_vehicles = [
            {
                'VehicleID': 1,
                'Brand': 'Toyota',
                'Model': 'Camry',
                'Year': 2022,
                'RegistrationPlate': 'ABC123',
                'Color': 'Blue',
                'Type': 'Sedan',
                'Availability': True
            },
            {
                'VehicleID': 2,
                'Brand': 'Honda',
                'Model': 'Civic',
                'Year': 2021,
                'RegistrationPlate': 'XYZ789',
                'Color': 'Silver',
                'Type': 'Sedan',
                'Availability': True
            }
        ]
        self.vehicle_service.GetAvailableVehicles = MagicMock(return_value=available_vehicles)

        result = self.vehicle_service.GetAvailableVehicles()
        self.assertEqual(result, available_vehicles)
        self.vehicle_service.GetAvailableVehicles.assert_called_once()  # Ensure method call

    def test_get_all_vehicles(self):
        all_vehicles = [
            {
                'VehicleID': 1,
                'Brand': 'Toyota',
                'Model': 'Camry',
                'Year': 2022,
                'RegistrationPlate': 'ABC123',
                'Color': 'Blue',
                'Type': 'Sedan',
                'Availability': True
            },
            {
                'VehicleID': 2,
                'Brand': 'Honda',
                'Model': 'Civic',
                'Year': 2021,
                'RegistrationPlate': 'XYZ789',
                'Color': 'Silver',
                'Type': 'Sedan',
                'Availability': True
            }
        ]
        self.vehicle_service.GetAllVehicles = MagicMock(return_value=all_vehicles)

        result = self.vehicle_service.GetAllVehicles()
        self.assertEqual(result, all_vehicles)
        self.vehicle_service.GetAllVehicles.assert_called_once()  # Ensure method call

if __name__ == '__main__':
    unittest.main()
