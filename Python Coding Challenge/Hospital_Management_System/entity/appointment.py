class Appointment:

    def __init__(self):
        self.__appointmentId = None
        self.__patientId = None
        self.__doctorId = None
        self.__appointmentDate = None
        self.__description = None

    def __init__(self, appointmentId, patientId, doctorId, appointmentDate, description):
        self.__appointmentId = appointmentId
        self.__patientId = patientId
        self.__doctorId = doctorId
        self.__appointmentDate = appointmentDate
        self.__description = description

    # Getter methods
    def getAppointmentId(self):
        return self.__appointmentId

    def getPatientId(self):
        return self.__patientId

    def getDoctorId(self):
        return self.__doctorId

    def getAppointmentDate(self):
        return self.__appointmentDate

    def getDescription(self):
        return self.__description

    # Setter methods
    def setAppointmentId(self, appointmentId):
        self.__appointmentId = appointmentId

    def setPatientId(self, patientId):
        self.__patientId = patientId

    def setDoctorId(self, doctorId):
        self.__doctorId = doctorId

    def setAppointmentDate(self, appointmentDate):
        self.__appointmentDate = appointmentDate

    def setDescription(self, description):
        self.__description = description

    def __str__(self):
        return f"Appointment ID: {self.__appointmentId}, Patient ID: {self.__patientId}, Doctor ID: {self.__doctorId}, Date: {self.__appointmentDate}, Description: {self.__description}"

    def printDetails(self):
        print(f"Appointment ID: {self.__appointmentId}")
        print(f"Patient ID: {self.__patientId}")
        print(f"Doctor ID: {self.__doctorId}")
        print(f"Date: {self.__appointmentDate}")
        print(f"Description: {self.__description}")