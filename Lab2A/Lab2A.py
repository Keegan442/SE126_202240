#Lab 2A
#Keegan Preston

#Program Prompt: The csv file lab2a.csv contains a list of rooms, the maximum number of people that the room can accommodate, and the number of people currently registered for the event.  Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that they will have to be put on the wait list. After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#Variable Dictionary:
#total_records - Total records completed
#over_rooms - Number of rooms over the limit
#over - Number of people over the limit

#MAIN CODE------------------------------------------------------------------------------------------------------------------------

import csv

total_records = 0
over_rooms = 0

print("{0:19} \t{1:5} \t{2:5} \t{3:5} ".format("Room", "Max", "Min", "Over"))

with open("Lab2A/lab2a.csv") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

        room = rec[0]
        max = int(rec[1])
        min = int(rec[2])
        over = 0

        if min > max:
            over = min - max
            over_rooms += 1
        
        print("{0:19} \t{1:0} \t{2:0} \t{3:5} ".format(room, max, min, over))

print("\nProcessed {0:0} records.".format(total_records))
print("There are {0:0} rooms over the limit.\n".format(over_rooms))