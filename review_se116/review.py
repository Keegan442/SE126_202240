#Week 1 Day 2 - SE116 Review Demo

#FUNCTIONS---------------------------------------------------------------------------------------
def capacity():

    cap = int(input("\tEnter the room's max capacity: "))
    return cap

#MAIN CODE---------------------------------------------------------------------------------------

print("\n\n\tWelcome to the Room Safety Manager!\n\n")

answer = input("\tWould you like to check some rooms? (y/n): ").lower()

while answer != "y" and answer != "n":

    print("\t\t**ERROR! INVALID ENTRY!**")
    answer = input("\tWould you like to check some rooms? (y/n): ").lower()

while answer == "y":

    roomCapacity = capacity()

    peopleAttending = int(input("\tEnter the number of meeting attendees for the room: "))

    difference = roomCapacity - peopleAttending

    if difference >= 0:
        print("\t\tSAFELY UNDER ROOM CAPACITY")
        print("\tYou may add up to {0} people to the meeting.".format(difference))
    
    else:
        print("\t\tOH NO! YOU ARE OVER ROOM CAPACITY")
        print("\tPlease remove at least {0} people from the meeting for safety regulations.".format(difference * -1))

    answer = input("\tWould you like to check some more rooms? (y/n): ").lower()

    while answer != "y" and answer != "n":

        print("\t\t**ERROR! INVALID ENTRY!**")
        answer = input("\tWould you like to check some rooms? (y/n): ").lower()

print("\n\n\tThank you for using my program! Goodbye! :] \n\n")