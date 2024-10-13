#task - 2

def calculateCostOfBooking(category, noOfTickets):
    Clist = {"silver":100, "gold":200, "diamond":3000}
    if category in Clist:
        basePrice = Clist[category]
        totalPrice = basePrice*noOfTickets
        print(f"Your total price is: {totalPrice}")

    else:
        print("Invalid ticket category")

category = input("Enter the category (gold, silver, diamond): ")
noOfTickets = int(input("Enter the number of tickets: "))
calculateCostOfBooking(category, noOfTickets)

#task - 3
while(True):
    category = input("Enter the category (gold, silver, diamond): ")
    if category == "Exit":
        break
    noOfTickets = int(input("Enter the number of tickets: "))

    calculateCostOfBooking(category, noOfTickets)