#Lab 4A
#Keegan Preston

#Program Prompt: 
#Process the lists to print the them as they appear in the file
#Re-process the lists to add the House Motto (dependent on Field4/Allegiance; see motto chart below)
#Re-Process the lists to print each record fully with the House Mottos
#Re-process the lists to find the average age within the list, then
#Print the total number of people in the list
#Print the average age
#Print tallies for each allegiance (Field4)

#Variable Dictionary

#MAIN CODE-----------------------------------------------------------------------------------------------------------------

import csv

records = 0
total_age = 0

firstname = []
lastname = []
age = []
nickname = []
house = []
motto = []


with open("Lab4A/lab4A_GOT_NEW.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        firstname.append(rec[0])
        lastname.append(rec[1])
        age.append(int(rec[2]))
        nickname.append(rec[3])
        house.append(rec[4])


print("{0:10}\t {1:10}\t {2}\t {3:15}\t {4:15}".format("FIRST", "LAST", "AGE", "NICKNAME", "HOUSE"))
for i in range(0, records):

    print("{0:10}\t {1:10}\t {2}\t {3:15}\t {4:15}".format(firstname[i], lastname[i], age[i], nickname[i], house[i]))

print("\n")

print("{0:10}\t {1:10}\t {2}\t {3:15}\t {4:15}\t {5:15}".format("FIRST", "LAST", "AGE", "NICKNAME", "HOUSE", "MOTTO"))
for i in range(0, records):

    if house[i] == "House Stark":
        house_motto = "Winter is Coming"
    elif house[i] == "House Baratheon":
        house_motto = "Ours is the Fury."
    elif house[i] == "House Tully":
        house_motto = "Family. Duty. Honor."
    elif house[i] == "Night's Watch":
        house_motto = "And now my watch begins."
    elif house[i] == "House Lannister":
        house_motto = "Hear me roar!"
    elif house[i] == "House Targaryen":
        house_motto = "Fire & Blood"
    
    motto.append(house_motto)

    print("{0:10}\t {1:10}\t {2}\t {3:15}\t {4:15}\t {5:15}".format(firstname[i], lastname[i], age[i], nickname[i], house[i], motto[i]))

stark_tally = ""
baratheon_tally = ""
tully_tally = ""
night_tally = ""
lannister_tally = ""
targaryen_tally = ""

for i in range(0, records):

    total_age += age[i]
    
    if house[i] == "House Stark":
        stark_tally += "|"
    if house[i] == "House Baratheon":
        baratheon_tally += "|"
    if house[i] == "House Tully":
        tully_tally += "|"
    if house[i] == "Night's Watch":
        night_tally += "|"
    if house[i] == "House Lannister":
        lannister_tally += "|"
    if house[i] == "House Targaryen":
        targaryen_tally += "|"

print("\n\t\t\t\t\t---ALLEGIANCE TALLIES---")
print("\t\tST: {0:5}\tBA: {1:5}\tTU: {2:5}\tNW: {3:5}\tLA: {4:5}\tTA: {5:5}".format(stark_tally, baratheon_tally, tully_tally, night_tally, lannister_tally, targaryen_tally))

avg_age = total_age / records

print("\nTotal number of people: {}".format(records))
print("Average age: {:.2f}\n".format(avg_age))