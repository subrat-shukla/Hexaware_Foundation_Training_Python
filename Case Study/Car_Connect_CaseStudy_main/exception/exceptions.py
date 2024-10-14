class AuthenticationException(Exception):
    def __init__(self, message="Authentication failed"):
        self.message = message
        super().__init__(self.message)


class ReservationException(Exception):
    def __init__(self, message="Reservation issue"):
        self.message = message
        super().__init__(self.message)


class CustomerNotFoundException(Exception):
    def __init__(self, message="Customer not found"):
        self.message = message
        super().__init__(self.message)


class VehicleNotFoundException(Exception):
    def __init__(self, message="Vehicle not found"):
        self.message = message
        super().__init__(self.message)


class ReservationNotFoundException(Exception):
    def __init__(self, message="Reservation not found"):
        self.message = message
        super().__init__(self.message)


class AdminNotFoundException(Exception):
    def __init__(self, message="Admin not found"):
        self.message = message
        super().__init__(self.message)


class InvalidInputException(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)


class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection issue"):
        self.message = message
        super().__init__(self.message)

