from abc import ABC, abstractmethod


class IAdminService(ABC):
    @abstractmethod
    def GetAdminById(self, admin_id):
        pass

    @abstractmethod
    def GetAdminByUsername(self, username):
        pass

    @abstractmethod
    def RegisterAdmin(self, admin_data):
        pass

    @abstractmethod
    def UpdateAdmin(self, admin_data):
        pass

    @abstractmethod
    def DeleteAdmin(self, admin_id):
        pass