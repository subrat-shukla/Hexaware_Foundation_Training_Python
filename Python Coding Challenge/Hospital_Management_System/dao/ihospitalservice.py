from abc import ABC, abstractmethod
from entity.appointment import Appointment
from typing import List

class IHospitalService(ABC):
    @abstractmethod
    def getAppointmentById(self, appointmentId) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self, patientId) -> List[Appointment]:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self, doctorId) -> List[Appointment]:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self, appointment: Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self, appointmentId) -> bool:
        pass