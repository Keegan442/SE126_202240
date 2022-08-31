import csv
from xml.sax.xmlreader import InputSource

id = []
name = []
age = []
color = []

records = 0

with open("binarySearch/binary-1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #print(rec)
        records += 1

        id.append(rec[0])
        name.append(rec[1])
        age.append(rec[2])
        color.append(rec[3])

print("Finished processing file. There are {} records.".format(records))

search = input("Get search from user! Enter LAST name: ")

min = 0

max = records - 1       #can also use len(listName) for 'records' value


guess = int((min + max) / 2)

#this is for INCREASING order

search_count = 0

while (min < max and search != name[guess]):

    search_count += 1

    if search < name[guess]:

        max = guess - 1

    else:

        min = guess + 1

    guess = int((min + max) / 2)

if search == name[guess]:

    #found them! use 'guess' for index of found search item
    print("Your search for {} was FOUND at index: {}".format(search, guess))
else:

    #boooo not found
    print("Your search for {} was NOT FOUND".format(search))

print("BINARY SEARCH LOOPS: {}".format(search_count))