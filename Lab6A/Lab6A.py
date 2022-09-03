#Lab 6A
#Keegan Preston

#Program Prompt: Write a Python program that reads the data from the file and stores all data into appropriate lists. The program should then prompt the user for the person’s last name they are searching for and display all available information on that person if they are found.  You must use the binary search method.  The program should allow the user to search for as many people as they want. The program should also print a statement telling the user how many iterations of the search loop the program went through before finding (or not finding) the requested person.

#Variable Dictionary:

#MAIN CODE--------------------------------------------------------------------------------------------------------------------------

import csv

records = 0

lastName = []
firstName = []
birthDay = []

with open("Lab6A/lab6A.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lastName.append(rec[0])
        firstName.append(rec[1])
        birthDay.append(rec[2])

for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:5}".format(lastName[i], firstName[i], birthDay[i]))

answer = 'y'

while answer == 'y':
    
    for i in range(0, records - 1):#outter loop

        print("OUTER LOOP! i = ", i)


        for index in range(0, records - 1):#inner loop

            print("\t INNER LOOP! k = ", index)

            #below if statement determines the sort

            #list used is the list being sorted

            # > is for increasing order, < for decreasing

            if(lastName[index] > lastName[index + 1]):

                print("\t\t SWAP! ", lastName[index], "<-->", lastName[index + 1])

                #if above is true, swap places!

                temp = lastName[index]

                lastName[index] = lastName[index + 1]

                lastName[index + 1] = temp

            
                #swap all other values

                temp = birthDay[index]

                birthDay[index] = birthDay[index + 1]

                birthDay[index + 1] = temp


                temp = firstName[index]
                firstName[index] = firstName[index + 1]
                firstName[index + 1] = temp


    print("\n\t\tBINARY SEARCH")

    search = input("Enter the lastname of the person you would like to search for: ").title()

    min = 0
    max = records - 1
    guess = int((min + max) / 2)
    searchCount = 0

    while min < max and search != lastName[guess]:

        searchCount += 1

        if search < lastName[guess]:

            max = guess - 1
        else:

            min = guess + 1

        guess = int((min + max) /2)
            
    if search == lastName[guess]:

        print("\nAMOUNT OF SEARCHES: ", searchCount,".")        
        print("\tYour BINARY SEARCH results for", search,": ")

                
        print("{0:15}\t{1:15}\t{2:5}".format(lastName[guess], firstName[guess], birthDay[guess]))
        answer = input("\n\tWould you like to search again? [y/n]: ")
    else:
        print("\tYour BINARY SEARCH results for", search," could NOT be found. ")
        answer = input("\n\tWould you like to search again? [y/n]: ")