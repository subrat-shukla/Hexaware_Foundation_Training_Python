from abc import ABC, abstractmethod


class IReservationService(ABC):
    @abstractmethod
    def GetReservationById(self, reservation_id):
        pass

    @abstractmethod
    def GetReservationsByCustomerId(self, customer_id):
        pass

    @abstractmethod
    def CreateReservation(self, reservation_data):
        pass

    @abstractmethod
    def UpdateReservation(self, reservation_data):
        pass

    @abstractmethod
    def CancelReservation(self, reservation_id):
        pass