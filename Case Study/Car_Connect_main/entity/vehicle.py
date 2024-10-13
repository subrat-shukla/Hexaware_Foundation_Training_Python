class Vehicle:
    def __init__(self, vehicle_id, model, make, year, color, registration_number, availability, daily_rate):
        self._vehicle_id = vehicle_id
        self._model = model
        self._make = make
        self._year = year
        self._color = color
        self._registration_number = registration_number
        self._availability = availability
        self._daily_rate = daily_rate

    def get_vehicle_id(self):
        return self._vehicle_id

    def get_model(self):
        return self._model

    def get_make(self):
        return self._make

    def get_year(self):
        return self._year

    def get_color(self):
        return self._color

    def get_registration_number(self):
        return self._registration_number

    def get_availability(self):
        return self._availability

    def get_daily_rate(self):
        return self._daily_rate

    def set_vehicle_id(self, vehicle_id):
        if isinstance(vehicle_id, int) and vehicle_id > 0:
            self._vehicle_id = vehicle_id
        else:
            print("Invalid vehicle_id. It should be a positive integer.")

    def set_model(self, model):
        if model:
            self._model = model
        else:
            print("Invalid model. It should not be empty.")

    def set_make(self, make):
        if make:
            self._make = make
        else:
            print("Invalid make. It should not be empty.")

    def set_year(self, year):
        if isinstance(year, int) and year > 0:
            self._year = year
        else:
            print("Invalid year. It should be a positive integer.")

    def set_color(self, color):
        if color:
            self._color = color
        else:
            print("Invalid color. It should not be empty.")

    def set_registration_number(self, registration_number):
        if registration_number:
            self._registration_number = registration_number
        else:
            print("Invalid registration_number. It should not be empty.")

    def set_availability(self, availability):
        self._availability = availability

    def set_daily_rate(self, daily_rate):
        if isinstance(daily_rate, (int, float)) and daily_rate >= 0:
            self._daily_rate = daily_rate
        else:
            print("Invalid daily_rate. It should be a non-negative number.")