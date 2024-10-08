class Doctor:

    def __init__(self):
        self.__doctorId = None
        self.__firstName = None
        self.__lastName = None
        self.__specialization = None
        self.__contactNumber = None

    def __init__(self, doctorId, firstName, lastName, specialization, contactNumber):
        self.__doctorId = doctorId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__specialization = specialization
        self.__contactNumber = contactNumber

    # Getter methods
    def getDoctorId(self):
        return self.__doctorId

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getSpecialization(self):
        return self.__specialization

    def getContactNumber(self):
        return self.__contactNumber

    # Setter methods
    def setDoctorId(self, doctorId):
        self.__doctorId = doctorId

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setSpecialization(self, specialization):
        self.__specialization = specialization

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def __str__(self):
        return f"Doctor ID: {self.__doctorId}, Name: {self.__firstName} {self.__lastName}, Specialization: {self.__specialization}, Contact: {self.__contactNumber}"

    def printDetails(self):
        print(f"Doctor ID: {self.__doctorId}")
        print(f"Name: {self.__firstName} {self.__lastName}")
        print(f"Specialization: {self.__specialization}")
        print(f"Contact: {self.__contactNumber}")