#WEEK 6 DAY 1: Sequential Search

#Sequential Search: Sequential search means to search through an entire list (array), starting at the first record and looking through every one until the last, when looking for something. 

 

#For Loops --> allow us to process every record in an list (for index in range(0, records) --> this applies to every record in the list)

#If Statements --> allow us to "search": compare a value in the list we are looking through against the value(s) we are looking for. 

#we are utilizing binary.txt for this demo
#       FIELD0     #FIELD1     FIELD2      FIELD3
#       ID nums    Names       Age         Color  

#VARIABLE DICTIONARY
#




#BASE PROGRAM CODE--------------------------------------------------------------------

import csv
from xml.sax.xmlreader import InputSource

id = []
name = []
age = []
color = []

records = 0

with open("SequentialSearch/binary.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)
        records += 1

        id.append(rec[0])
        name.append(rec[1].lower())
        age.append(rec[2])
        color.append(rec[3].lower())

print("Finished processing file. There are {} records.".format(records))

for i in range(0, records):
    print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(i, id[i], name[i].title(), age[i], color[i].title()))

print("\n\n\n")

answer = "y"

while answer == "y":

    search_count = 0

    search = input("Enter the full LAST NAME of the record you are looking for: ").lower()
    found = []
    for i in range(0, records):

        search_count += 1

        if search == name[i]:

            found.append(i)

    print("\n\nSEQUENTIAL SEARCH COMPLETE.")
    if len(found) > 0:
        print("Your search for '{}' was found.".format(search))

        for i in range(0, len(found)):
            print("INDEX: {0} \t {1:10} \t {2:10} \t {3:10} \t {4:10}".format(found[i], id[found[i]], name[found[i]].title(), age[found[i]], color[found[i]].title()))

    else:
        print("Your search for '{}' was NOT found.".format(search))
    
    print("Search Loop Iterations Performed: {}".format(search_count))

    answer = input("\nEnter 'y' to search again: [y/n] ").lower()

    while answer != "y" and answer != "n":
        print("\t\tERROR! INVALID INPUT!")
        answer = input("\nEnter 'y' to search again: [y/n] ").lower()

print("\n\n\t\tTHANKS FOR USING MY PROGRAM!")