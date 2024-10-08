class Patient:
    
    def __init__(self):
        self.__patientId = None
        self.__firstName = None
        self.__lastName = None
        self.__dateOfBirth = None
        self.__gender = None
        self.__contactNumber = None
        self.__address = None

    def __init__(self, patientId, firstName, lastName, dateOfBirth, gender, contactNumber, address):
        self.__patientId = patientId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__dateOfBirth = dateOfBirth
        self.__gender = gender
        self.__contactNumber = contactNumber
        self.__address = address

    # Getter methods
    def getPatientId(self):
        return self.__patientId

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getDateOfBirth(self):
        return self.__dateOfBirth

    def getGender(self):
        return self.__gender

    def getContactNumber(self):
        return self.__contactNumber

    def getAddress(self):
        return self.__address

    # Setter methods
    def setPatientId(self, patientId):
        self.__patientId = patientId

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setDateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def setGender(self, gender):
        self.__gender = gender

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def setAddress(self, address):
        self.__address = address

    def __str__(self):
        return f"Patient ID: {self.__patientId}, Name: {self.__firstName} {self.__lastName}, DOB: {self.__dateOfBirth}, Gender: {self.__gender}, Contact: {self.__contactNumber}, Address: {self.__address}"
    
    def printDetails(self):
        print(f"Patient ID: {self.__patientId}")
        print(f"Name: {self.__firstName} {self.__lastName}")
        print(f"DOB: {self.__dateOfBirth}")
        print(f"Gender: {self.__gender}")
        print(f"Contact: {self.__contactNumber}")
        print(f"Address: {self.__address}")