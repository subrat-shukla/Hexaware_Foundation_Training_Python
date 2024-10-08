class PatientNumberNotFoundException(Exception):
    def __init__(self, patientId):
        super().__init__(f"Patient with ID {patientId} not found.")