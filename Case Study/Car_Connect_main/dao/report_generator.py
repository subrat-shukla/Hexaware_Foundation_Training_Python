
class ReportGenerator:
    @staticmethod
    def generate_reservation_report(reservation_data):
        print("Reservation Report:")
        print("Reservation ID | Customer ID | Vehicle ID | Start Date | End Date | Amount | Status")
        for reservation in reservation_data:
            print(
                f"{reservation[0]:<15} | {reservation[1]:<12} | {reservation[2]:<11} | "
                f"{reservation[3]:<11} | {reservation[4]:<9} | {reservation[5]:<6} | {reservation[6]}")

    @staticmethod
    def generate_vehicle_report(vehicle_data):
        print("\nVehicle Report:")
        print("Vehicle ID | Model | Brand | Year | Color")
        for vehicle in vehicle_data:
            print(f"{vehicle[0]:<11} | {vehicle[1]:<5} | {vehicle[2]:<6} | {vehicle[3]:<4} | {vehicle[4]}")