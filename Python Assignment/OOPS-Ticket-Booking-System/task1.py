def checkBookingTicket(availableTicket, noOfBookingTicket):
    if availableTicket >= noOfBookingTicket:
        remainingticket = availableTicket - noOfBookingTicket
        print(f"Remaining Tikets are {remainingticket}")
    else:
        print("No  available tickets ")

availableTicket = int(input("Enter the available tickets: "))
noOfBookingTicket = int(input("Enter the number of booking tickets: "))
checkBookingTicket(availableTicket, noOfBookingTicket)