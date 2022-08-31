#Lab 5
#Keegan Preston

#Program Prompt: Re-write the Week #5 Class Lab but instead of searching for a person’s name, search for their birthday.  If the person is found, reprint their entire record to the console.  The program should allow the user to search for as many birthdays as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person

#Variable Dictionary:

#MAIN CODE------------------------------------------------------------------------------------------------------------------------
import csv

records = 0

lName = []
fName = []
bDay = []
year = []

with open("Lab5\lab5_updated.txt") as csvfile:
    
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lName.append(rec[0])
        fName.append(rec[1])
        bDay.append(rec[2])
        year.append(int(rec[3]))

print("Finished processing file. There are {} records.".format(records))

print("          \t {0:10} \t {1:10} \t {2:10}".format("LAST NAME", "FIRST NAME", "BIRTHDAY"))
for i in range(0, records):
    print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10}".format(i, lName[i], fName[i], bDay[i]))

print("\n\n\n")

answer = "y"

while answer == "y":

    search_count = 0

    search = input("Enter the full birthday date of the person you want to search for [00/00/0000]: ")
    found = []

    for i in range(0, records):

        search_count += 1

        if search == bDay[i]:
            currentAge = 2022 - year[i]
            found.append(i)
        
    print("\n\nSEQUENTIAL SEARCH COMPLETE.")
    if len(found) > 0:

        for i in range(0, len(found)):
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10}".format(found[i], lName[found[i]], fName[found[i]], bDay[found[i]]))
            print("Their current age is {}.".format(currentAge))

    else:
        print("Your search for {} was NOT FOUND.".format(search))
    
    print("Search Loop Iterations Performed: {}".format(search_count))

    answer = input("\nEnter 'y' to search again: [y/n] ").lower()

    while answer != "y" and answer != "n":
        print("\t\tERROR! INVALID INPUT!")
        answer = input("\nEnter 'y' to search again: [y/n] ").lower()