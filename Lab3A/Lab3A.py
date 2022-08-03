#Lab #3A
#Keegan Preston

#Program Prompt: Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.

#Variable Dictionary:
#records - number of records
#device - device type
#brand - brand name
#cpu - cpu type
#ram - ram type (8GB/16GB)
#first_disk - space on first disk
#num_hdd - number of hard drives
#second_disk - space on second disk (if there is one)
#os - operating system
#yr - year of the device
#ram8 - number of 8GB ram
#ram16 - number of 16GB ram
#numDesk - number of desktops out of date
#numLap - number of laptops out of date
#priceDesk - cost to replace the out of date desktops
#priceLap - cost to replace the out of date laptops



#MAIN CODE----------------------------------------------------------------------------------------------------------------------
import csv

records = 0

#prepare empty lists - one for every possible field in the file
device = []
brand = []
cpu = []
ram = []
first_disk = []
num_hdd = []
second_disk = []
os = []
yr = []

with open("Lab3A/lab3a.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1
        
        
        #add data from file to lists - .append()
        device.append(rec[0])
        brand.append(rec[1])
        cpu.append(rec[2])
        ram.append(rec[3])
        first_disk.append(rec[4])
        num_hdd.append(rec[5])

        if rec[5] == "1":
            second_disk.append("-none-")
            os.append(rec[6])
            yr.append(int(rec[7]))

        
        else:
            second_disk.append(rec[6])
            os.append(rec[7])
            yr.append(int(rec[8]))
        

print("\n\tORIGINAL FILE DATA---------------------------------------------------------------------")

for index in range(0, records):

    if device[index] == "D":
        device[index] = "Desktop"
    elif device[index] == "L":
        device[index] = "Laptop"

    print("INDEX#{9}:\t{0:8}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}".format(device[index], brand[index], cpu[index], ram[index], first_disk[index], num_hdd[index], second_disk[index], os[index], yr[index], index))

print("\n\t---------------------------------------------------------------------------------------")
print("\n\n\tTOTAL RECORDS: ", records)

ram8 = 0
ram16 = 0
numDesk = 0
numLap = 0

for index in range(0, records):

    if ram[index] == "08":

        ram8 += 1
    elif ram[index] == "16":

        ram16 += 1
    
    if yr[index] <= 16 and device[index] == "Desktop":

        numDesk += 1
    elif yr[index] <= 16 and device[index] == "Laptop":

        numLap += 1

priceDesk = numDesk * 2000
priceLap = numLap * 1500
print("\n\tTHERE ARE {0} 8GB RAM DEVICES / {1} 16GB RAM DEVICES".format(ram8, ram16))
print("\n\tTHERE ARE {0} DESKTOPS THAT NEED TO BE REPLACED, IT WILL COST ${1} TO REPLACE THEM".format(numDesk, priceDesk))
print("\n\tTHERE ARE {0} LAPTOPS THAT NEED TO BE REPLACED, IT WILL COST ${1} TO REPLACE THEM".format(numLap, priceLap))