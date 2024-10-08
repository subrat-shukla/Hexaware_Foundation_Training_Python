from dao.hospitalserviceimpl import HospitalServiceImpl
from entity.appointment import Appointment
from exception.patient_exception import PatientNumberNotFoundException

def get_user_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Input cannot be empty. Please try again.")

def main():
    print("      Hospital Management System      \n")
    try:
        # Instantiate the HospitalServiceImpl class
        hospital_service = HospitalServiceImpl()

        while True:
            print("Choose a number:")
            print("1. Search by appointment ID")
            print("2. Search by Patient ID")
            print("3. Search by Doctor ID")
            print("4. Book an Appointment")
            print("5. Update an Appointment")
            print("6. Cancel an Appointment")
            print("7. Exit")
            
            choice = get_user_input("Enter your number: ")
            
            if choice == '1':
                appointment_id = int(get_user_input("Enter appointment ID: "))
                appointment = hospital_service.getAppointmentById(appointment_id)
                print("Appointment by ID:", appointment)
                
            elif choice == '2':
                patient_id = get_user_input("Enter patient ID: ")
                appointments_for_patient = hospital_service.getAppointmentsForPatient(patient_id)
                print(f"Appointments for Patient {patient_id}:")
                for appt in appointments_for_patient:
                    print(appt)
                    
            elif choice == '3':
                doctor_id = get_user_input("Enter doctor ID: ")
                appointments_for_doctor = hospital_service.getAppointmentsForDoctor(doctor_id)
                print(f"Appointments for Doctor {doctor_id}:")
                for appt in appointments_for_doctor:
                    print(appt)
                    
            elif choice == '4':
                # Create a new appointment
                new_appointment = Appointment(appointmentId=int(get_user_input("Enter appointment ID: ")),
                                              patientId=get_user_input("Enter patient ID: "),
                                              doctorId=get_user_input("Enter doctor ID: "),
                                              appointmentDate=get_user_input("Enter appointment date (YYYY-MM-DD): "),
                                              description=get_user_input("Enter description: "))
                success = hospital_service.scheduleAppointment(new_appointment)
                print("Appointment Scheduled:", success)
                
            elif choice == '5':
                # Update an existing appointment
                existing_appointment = Appointment(appointmentId=int(get_user_input("Enter appointment ID: ")),
                                                   patientId=get_user_input("Enter patient ID: "),
                                                   doctorId=get_user_input("Enter doctor ID: "),
                                                   appointmentDate=get_user_input("Enter appointment date (YYYY-MM-DD): "),
                                                   description=get_user_input("Enter description: "))
                success = hospital_service.updateAppointment(existing_appointment)
                print("Appointment Updated:", success)
                
            elif choice == '6':
                appointment_to_cancel = int(get_user_input("Enter appointment ID to cancel: "))
                success = hospital_service.cancelAppointment(appointment_to_cancel)
                print("Appointment Canceled:", success)
                
            elif choice == '7':
                print("Exiting...")
                break
                
            else:
                print("Invalid choice. Please select a valid option.")
                
    except PatientNumberNotFoundException as e:
        print(f"Caught PatientNumberNotFoundException: {e}")
    except Exception as e:
        print(f"Unexpected exception: {e}")

if __name__ == "__main__":
    main()
