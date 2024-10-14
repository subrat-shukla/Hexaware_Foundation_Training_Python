import re
from datetime import datetime


class Admin:
    def __init__(self, admin_id, first_name, last_name, email, phone_number, username, password, role, join_date):
        self._admin_id = admin_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone_number = phone_number
        self._username = username
        self._password = password
        self._role = role
        self._join_date = join_date

    def get_admin_id(self):
        return self._admin_id

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phone_number

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_role(self):
        return self._role

    def get_join_date(self):
        return self._join_date

    def set_admin_id(self, admin_id):
        if isinstance(admin_id, int) and admin_id > 0:
            self._admin_id = admin_id
        else:
            print("Invalid admin_id. It should be a positive integer.")

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

    def set_role(self, role):
        self._role = role

    def set_join_date(self, join_date):
        try:
            datetime.strptime(join_date, "%Y-%m-%d")
            self._join_date = join_date
        except ValueError:
            print("Invalid join_date format.")

    def authenticate(self, input_password):
        return input_password == self._password

    @classmethod
    def create_from_input(cls):
        admin_id = int(input("Enter AdminID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        role = input("Enter Role: ")
        join_date = input("Enter Join Date (YYYY-MM-DD): ")
        print("Admin created successfully ")
        return cls(admin_id, first_name, last_name, email, phone_number, username, password, role, join_date)


admin_instance = Admin.create_from_input()
print("Authentication method")
input_password = input("Enter your password: ")

if admin_instance.authenticate(input_password):
    print("Authentication successfully ")
else:
    print("Authentication failed. Incorrect password.")