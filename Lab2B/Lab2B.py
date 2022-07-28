#Lab #2B
#Keegan Preston

#Program Prompt: You have been asked to produce a report that lists all the computers in the csv file lab2b.csv. Your report should look like the following sample output.  The last line should print the number of computers in the file.

#Variable Dictionary:


#MAIN CODE----------------------------------------------------------------------------------------------------------------------
import csv

print("{0:8} \t{1:8} \t{2:8} \t{3:8} \t{4:8} \t{5:8} \t{6:8} \t{7:8} \t{8:8} ".format("Type", "Brand", "CPU", "RAM", "1st Disk", "No. HDD", "2nd Disk", "OS", "YR"))

with open("Lab2B/lab2b.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        type = rec[0]
        brand = rec[1]
        cpu = rec[2]
        ram = rec[3]
        disk1 = rec[4]
        numHDD = int(rec[5])
        
        if type == "D":
            type = "Desktop"
        elif type == "L":
            type = "Laptop"
        
        if brand == "DL":
            brand = "Dell"
        elif brand == "HP":
            brand = "HP"
        elif brand == "GW":
            brand = "Gateway"

        if numHDD == 1:
            os = rec[6]
            year = rec[7]

            print("{0:8} \t{1:8} \t{2:8} \t{3:8} \t{4:8} \t{5:8} \t{6:8} \t{7:8} \t{8:8} ".format(type, brand, cpu, ram, disk1, numHDD, "    ", os, year))
        elif numHDD == 2:
            disk2 = rec[6]
            os = rec[7]
            year = rec[8]

            print("{0:8} \t{1:8} \t{2:8} \t{3:8} \t{4:8} \t{5:8} \t{6:8} \t{7:8} \t{8:8} ".format(type, brand, cpu, ram, disk1, numHDD, disk2, os, year))