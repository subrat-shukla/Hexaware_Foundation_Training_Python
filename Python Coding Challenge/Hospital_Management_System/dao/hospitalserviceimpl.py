import pyodbc
from dao.ihospitalservice import IHospitalService
from entity.appointment import Appointment
from util.dbConnection import DBConnection
from exception.patient_exception import PatientNumberNotFoundException
from typing import List

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def getAppointmentById(self, appointmentId) -> Appointment:
        self.cursor.execute("SELECT * FROM appointment WHERE appointmentId=?", (appointmentId,))
        result = self.cursor.fetchone()
        if result:
            appointment = Appointment(*result)
            return appointment
        return None


    def getAppointmentsForPatient(self, patientId) -> List[Appointment]:
        try:
            self.cursor.execute("SELECT * FROM appointment WHERE patientId=?", (patientId,))
            results = self.cursor.fetchall()
            if not results:
                raise PatientNumberNotFoundException(patientId)
            
            appointment = [Appointment(*row) for row in results]
            return appointment
        except PatientNumberNotFoundException as e:
            # Log or handle the exception as needed
            print(f"Exception: {e}")
            return []
        except Exception as e:
            # Log or handle other exceptions
            print(f"Unexpected exception: {e}")
            return []

    def getAppointmentsForDoctor(self, doctorId) -> List[Appointment]:
        self.cursor.execute("SELECT * FROM appointment WHERE doctorId=?", (doctorId,))
        results = self.cursor.fetchall()
        appointment = [Appointment(*row) for row in results]
        return appointment

    def scheduleAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                INSERT INTO appointment (appointmentId, patientId, doctorId, 
                appointmentDate, description) VALUES (?, ?, ?, ?, ?)
            """, (appointment.getAppointmentId(), appointment.getPatientId(),
                  appointment.getDoctorId(), appointment.getAppointmentDate(),
                  appointment.getDescription()))
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error scheduling appointment: {e}")
            return False

    def updateAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""
                UPDATE appointment
                SET patientId=?, doctorId=?, appointmentDate=?, description=?
                WHERE appointmentId=?
            """, (appointment.getPatientId(), appointment.getDoctorId(),
                  appointment.getAppointmentDate(), appointment.getDescription(),
                  appointment.getAppointmentId()))
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error updating appointment: {e}")
            return False

    def cancelAppointment(self, appointmentId) -> bool:
        try:
            self.cursor.execute("DELETE FROM appointment WHERE appointmentId=?",
                                (appointmentId,))
            self.conn.commit()
            return True
        except pyodbc.Error as e:
            print(f"Error canceling appointment: {e}")
            return False