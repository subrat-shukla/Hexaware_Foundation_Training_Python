import re
from datetime import datetime


class Customer:
    def __init__(self, customer_id, first_name, last_name, email, phone_number, address, username, password,
                 registration_date):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._address = address
        self._username = username
        self._password = password
        self._registration_date = registration_date

    def get_customer_id(self):
        return self._customer_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_address(self):
        return self._address

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_registration_date(self):
        return self._registration_date

    def set_customer_id(self, customer_id):
        if isinstance(customer_id, int) and customer_id > 0:
            self._customer_id = customer_id
        else:
            print("Invalid customer_id. It should be a positive integer.")

    def set_first_name(self, first_name):
        if first_name:
            self._first_name = first_name
        else:
            print("Invalid first_name. It should not be empty.")

    def set_last_name(self, last_name):
        if last_name:
            self._last_name = last_name
        else:
            print("Invalid last_name. It should not be empty.")

    def set_email(self, email):
        if email and re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self._email = email
        else:
            print("Invalid email format.")

    def set_phone_number(self, phone_number):
        if phone_number and re.match(r"\d{10}", phone_number):
            self._phone_number = phone_number
        else:
            print("Invalid phone number format.")

    def set_address(self, address):
        if address:
            self._address = address
        else:
            print("Invalid address. It should not be empty.")

    def set_username(self, username):
        if username:
            self._username = username
        else:
            print("Invalid username. It should not be empty.")

    def set_password(self, password):
        if password:
            self._password = password
        else:
            print("Invalid password. It should not be empty.")

    def set_registration_date(self, registration_date):
        try:
            datetime.strptime(registration_date, "%Y-%m-%d")
            self._registration_date = registration_date
        except ValueError:
            print("Invalid registration_date format.")

    def authenticate(self, input_password):
        return input_password == self._password

    @classmethod
    def create_from_input(cls):
        customer_id = int(input("Enter CustomerID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        registration_date = input("Enter Registration Date (YYYY-MM-DD): ")
        print("Customer Created Successfully ")
        return cls(customer_id, first_name, last_name, email, phone_number, address, username, password,
            registration_date)


customer_instance = Customer.create_from_input()
print("Authentication method")
input_password = input("Enter your password: ")

if customer_instance.authenticate(input_password):
    print("Authentication successful!")
else:
    print("Authentication failed. Incorrect password.")