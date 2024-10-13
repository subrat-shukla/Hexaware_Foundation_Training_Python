from abc import ABC, abstractmethod


class IVehicleService(ABC):
    @abstractmethod
    def GetVehicleById(self, vehicle_id):
        pass

    @abstractmethod
    def GetAvailableVehicles(self):
        pass

    @abstractmethod
    def AddVehicle(self, vehicle_data):
        pass

    @abstractmethod
    def UpdateVehicle(self, vehicle_data):
        pass

    @abstractmethod
    def RemoveVehicle(self, vehicle_id):
        pass