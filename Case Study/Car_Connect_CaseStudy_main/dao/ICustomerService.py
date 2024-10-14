from abc import ABC, abstractmethod


class ICustomerService(ABC):
    @abstractmethod
    def GetCustomerById(self, customer_id):
        pass

    @abstractmethod
    def GetCustomerByUsername(self, username):
        pass

    @abstractmethod
    def RegisterCustomer(self, customer_data):
        pass

    @abstractmethod
    def UpdateCustomer(self, customer_data):
        pass

    @abstractmethod
    def DeleteCustomer(self, customer_id):
        pass