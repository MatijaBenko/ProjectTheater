import csv
import sys
import os.path

def userInput_check(bound):
    if(isinstance(bound,float)):
        while(True):
            try:
                userInput = float(
                input("Enter option (LIMIT 0-" + str(bound) + "): "))
            except(NameError, SyntaxError, ValueError, TypeError):
                print("---Invalid Input---")
                continue
            else:
                if(userInput >= 0 and userInput <= bound):
                    return userInput
                else:
                    print("---Opition Not Available---")
    else:
        while(True):
            try:
                userInput = int(
                    input("Enter option (LIMIT 0-" + str(bound) + "): "))
            except(NameError, SyntaxError, ValueError,TypeError):
                print("---Invalid Input---")
                continue
            else:
                if(userInput >= 0 and userInput <= bound):
                    return userInput
                else:
                    print("---Opition Not Available---")


def check_Row():
    while(True):
        try:
            row = int(input("Enter total row (LIMIT 1-5): "))
        except(NameError, SyntaxError, ValueError):
            print("---Invalid Input---")
            continue
        else:
            if(row > 0 and row <= 5):
                return row
            else:
                print("---Exceeding Limit---")


def check_Column():
    while(True):
        try:
            column = int(input("Enter total column (LIMIT 1-30): "))
        except(NameError, SyntaxError, ValueError):
            print("---Invalid Input---")
            continue
        else:
            if(column > 0 and column <= 30):
                return column
            else:
                print("---Exceeding Limit---")


# Create Threater in .csv File
def create_theater(seatContainer, file_csv):
    rowCost = []
    with open(file_csv, "w") as f:
        theater = csv.writer(f)
        # Writes all the open seats in the file
        for eachRow in range(len(seatContainer)):
            theater.writerow("#" * len(seatContainer[0]))

    #Writes the Cost For designated Row
    with open("cost.txt", "w") as file:
        print("------CHOOSING COST FOR ROWS------")
        for eachRow in range(len(seatContainer)):
            print("ROW #" + str(eachRow))
            userInput = userInput_check(100.0)
            rowCost.append(userInput)
            bracketSlice = str(rowCost)[1:-1]
        file.write(bracketSlice)


# Update all the Seats and display
def update_theater(seatContainer):
    with open("theater.csv", "w") as f:
        w = csv.writer(f)
        for eachRow in seatContainer:
            w.writerow(eachRow)


# Print Display of Seats
def print_seats(file_name):
    rowNumber = 1
    #List Holder for Seats
    allSeats = list()

    #Append all seats from csv file to the list holder
    with open(file_name, "r") as file:
        seats = csv.reader(file)
        for row in seats:
            allSeats.append(row)

    #Prints Seat Interface
    sys.stdout.write("      ")
    for eachColumn in range(len(allSeats[0])):
        sys.stdout.write(str(eachColumn % 10))
    print("")
    for eachRow in allSeats:
        sys.stdout.write("Row " + str(rowNumber-1) + " ")
        for eachSeat in eachRow:
            sys.stdout.write(eachSeat)
        print("")
        rowNumber += 1



#Clears CSV & TXT File
def clear_file(file_name):
    with open(file_name, "w") as file:
        file.truncate()
    with open("cost.txt", "w") as file:
        file.truncate(0)


# Checks the sales cost and Update the Seat
def sale(seatContainer):
    rowCost = []
    checkGroupSeats = False
    totalGroup = 0

    #Save Cost of Seat In eachRow in rowCost list
    with open("cost.txt", "r") as txtFile:
        for line in txtFile:
            costOfRow = line.split(", ")
            for eachCost in range(len(seatContainer)):
                rowCost.append(costOfRow[eachCost])

    print("(0) Selling Singular Ticket")
    print("(1) Selling Group Tickets")
    userInput = userInput_check(1)
    if(userInput == 0):
        row = userInput_check(len(seatContainer)-1)
        column = userInput_check(len(seatContainer[0]))

        #Update CSV File if Seat is Available 
        if(seatContainer[row][column] != "*"):
            print("")
            print("=====SEAT [" + str(row) + "][" +
                  str(column) + "] IS NOW TAKEN=====")
            print("")
            seatContainer[row][column] = "*"
            print("\t$"+str(rowCost[row]) + " Purchased")
        else:

            print("===SEAT [" + str(row) + "][" +
                  str(column) + "] IS UNAVAILABLE===")
        update_theater(seatContainer)
    elif(userInput == 1):
        mainRow = userInput_check(len(seatContainer)-1)
        column1 = userInput_check(len(seatContainer[0]))
        column2 = userInput_check(len(seatContainer[0]))

        #Checks if row of Seats is Available
        for eachSeat in range(column1, column2):
            if(seatContainer[mainRow][eachSeat] != "*"):
                checkGroupSeats = True
            else:
                print("SEAT #" + str(eachSeat) + " IS TAKEN TRY AGAIN")
                break

        #Updates CSV File and SeatContainer List
        if(checkGroupSeats):
            for eachSeat in range(column1, column2):
                totalGroup += 1
                seatContainer[mainRow][eachSeat] = "*"
                print("=====SEAT [" + str(mainRow) + "][" +
                  str(eachSeat) + "] IS NOW TAKEN=====")
        totalPrice = totalGroup * float(rowCost[mainRow])
        print("\t$"+str(totalPrice) + " Purchased")
        update_theater(seatContainer)


# Prints Report
def display_statistics(seatContainer):
    rowCost = []
    rowIndex = 0
    totalTicketsPurchase, totalTicketsPerRow, totalSeatsAvailable = 0, 0, 0
    totalRevenue = 0.0

    #Reads in the Cost Per Seat Given Row and Adds to rowCost lis
    with open("cost.txt", "r") as txtFile:
        for line in txtFile:
            costOfRow = line.split(", ")
            for eachCost in range(len(seatContainer)):
                rowCost.append(costOfRow[eachCost])
    
    #Tallies the amount of Tickets Bought
    for eachRow in seatContainer:
        for eachColumn in eachRow:
            if(eachColumn != "#"):
                totalTicketsPurchase += 1
                totalTicketsPerRow += 1

            else:
                totalSeatsAvailable += 1
            totalRevenue += (float(rowCost[rowIndex]) * totalTicketsPerRow)
            totalTicketsPerRow = 0
        rowIndex+=1
    print("TOTAL TICKETS: " + str(totalTicketsPurchase))
    print("TOTAL REVENUE: $"+ "%.2f" % totalRevenue)
    print("TOTAL SEATS AVAILABLE: " +str(totalSeatsAvailable))

    


# Main Menu
def main_interface():
    seatContainer = list()
    row = 0
    # Interface Print Out Titles
    dash = "=" * 40
    title = "-"

    exitLoop = True
    csvFile_Created = os.path.exists("theater.csv")
    csvFileIs_Empty = True

    # Checks if file is cleared
    if(csvFile_Created == True):
        if os.path.getsize("theater.csv") > 0:
            csvFileIs_Empty = False

    # Recreates file info for seats if file is not created or file is empty
    if(not csvFile_Created or csvFileIs_Empty):
        # Header
        print(dash + "\n" + title*11 + "Creating New File" + title * 11)
        print(dash)

        # Two-D Array
        row = check_Row()
        column = check_Column()
        seatContainer = [[0 for col in range(column)] for rows in range(row)]

        # csv & txt file created
        create_theater(seatContainer, "theater.csv")

        # Header
        print(dash + "\n" + title*13 + "Please Restart" + title * 13)
        print(dash)

    # Check if file is created and file is not empty
    if(csvFile_Created and not csvFileIs_Empty):
        while(exitLoop):
            seatContainer *= 0
            with open("theater.csv", "r") as f:
                r = csv.reader(f)
                for eachRow in r:
                    seatContainer.append(eachRow)
            # Interface Print Out Titles & Commands
            print(dash)
            print(title * 16 + "THEATER" + title * 16)
            print(dash + "\n")

            print("(0) Display All Seats")
            print("(1) Selling Ticket")
            print("(2) Display Statistics")
            print("(3) Reset Theater")
            print("(4) Exit")
            userInput = userInput_check(4)

            if(userInput == 0):
                print("Display Seats")
                print_seats("theater.csv")

            elif(userInput == 1):
                sale(seatContainer)

            elif(userInput == 2):
                display_statistics(seatContainer)

            elif(userInput == 3):
                print(dash + "\n" + title*13 + "File Resetted" + title * 13)
                print(dash)

                clear_file("theater.csv")
                csvFile_Created = False
                exitLoop = False

                print(dash + "\n" + title*13 + "Please Restart" + title * 13)
                print(dash)
                
            elif(userInput == 4):
                print(dash)
                print(title * 12 + "Exiting Program" + title * 12)
                print(dash)
                exitLoop = False


main_interface()
