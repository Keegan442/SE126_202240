#Lab 7
#Keegan Preston

#Program Prompt: Write a program that gives the user a menu of options to search through the file. Depending on how the user wants to search, you may need to sort the searched-through list before performing Binary Search. Binary Search should be used for Menu Options 1 (First Name) and 2 (ID codes) and the full record for the individual searched should be included if found (the user should be alerted if the person cannot be found).  If the user chooses options 3 or 4, you must print a list of everyone and their full record that fits the searched item (think: sequential search!) that has that Last Name or Allegiance.  Use the GOT_bubble_sort_7.txt file (you may change the name if you wish but you may NOT edit the text file outside of checking for and deleting empty end records).  The user should be able to search as many times as they would like.  If the user enters an option that does not exist, the program must tell them this before asking if the user would like to search for a new record.

#Variable Dictionary:

#Functions:
def menu():
    os.system('cls')

    print("\n\tSEARCH OPTIONS")
    print("1. Search by FIRST NAME")
    print("2. Search by ID CODE")
    print("3. Search by LAST NAME")
    print("4. Search by ALLEGIANCE")
    print("5. EXIT")

    choice = input("\nWhat would you like to do? [1-5]: ")

    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("\t\t**ERROR** INVALID ENTRY!")
        choice = input("\nWhat would you like to do? [1-5]: ")
    
    return choice

def nameSort():
    for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(firstName[index] > firstName[index + 1]):

                    print("\t\t SWAP! ", firstName[index], "<-->", firstName[index + 1])

                    #if above is true, swap places!

                    temp = firstName[index]

                    firstName[index] = firstName[index + 1]

                    firstName[index + 1] = temp

        
                    #swap all other values

                    temp = age[index]

                    age[index] = age[index + 1]

                    age[index + 1] = temp


                    temp = lastName[index]
                    lastName[index] = lastName[index + 1]
                    lastName[index + 1] = temp

                    temp = iD[index]
                    iD[index] = iD[index + 1]
                    iD[index + 1] = temp

                    temp = allegiance[index]
                    allegiance[index] = allegiance[index + 1]
                    allegiance[index + 1] = temp

def codeSort():
    for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(iD[index] > iD[index + 1]):

                    print("\t\t SWAP! ", iD[index], "<-->", iD[index + 1])

                    #if above is true, swap places!

                    temp = iD[index]

                    iD[index] = iD[index + 1]

                    iD[index + 1] = temp

        
                    #swap all other values

                    temp = age[index]

                    age[index] = age[index + 1]

                    age[index + 1] = temp


                    temp = lastName[index]
                    lastName[index] = lastName[index + 1]
                    lastName[index + 1] = temp

                    temp = firstName[index]
                    firstName[index] = firstName[index + 1]
                    firstName[index + 1] = temp

                    temp = allegiance[index]
                    allegiance[index] = allegiance[index + 1]
                    allegiance[index + 1] = temp

def repeat():
    ans = input("\n\tWould you like to search again? [y/n]: ")
    if ans != "y" and ans != "Y" and ans != "n" and ans != "N":
        print("**ERROR!** Invalid input!")
        ans = input("\n\tWould you like to search again? [y/n]: ")
    
    return ans

def goodbye():
    print("\n\tThank you for using my program and 'Never forget who you are...'")

#MAIN CODE--------------------------------------------------------------------------------------------------------------------------

import os
import csv

records = 0

iD = []
lastName = []
firstName = []
age = []
allegiance = []

with open("Lab7/GOT_bubble_sort_7.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        iD.append(rec[0])
        lastName.append(rec[1])
        firstName.append(rec[2])
        age.append(rec[3])
        allegiance.append(rec[4])

print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}\n".format("ID", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}".format(iD[i], lastName[i], firstName[i], age[i], allegiance[i]))

answer = input("\nWould you like to start searching? [y/n]: ")

while answer == "y":

    choice = menu()
    
    if choice == "1":
        
        nameSort()
    
        print("\n\t\tBINARY SEARCH")

        search = input("Enter the firstname of the person you are looking for: ").title()

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != firstName[guess]:

            if search < firstName[guess]:

                max = guess - 1
                
            else:

                min = guess + 1

            guess = int((min + max) /2)
            
        if search == firstName[guess]:
                
            print("\t\tYour BINARY SEARCH results for", search,": ")

            print("\n{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}\n".format("ID", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))    
            print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}".format(iD[guess], lastName[guess], firstName[guess], age[guess], allegiance[guess]))
            answer = repeat()
            
        else:
            print("\t\tYour BINARY SEARCH results for", search," could NOT be found. ")
            answer = repeat()
    
    if choice == "2":
        
        codeSort()
    
        print("\n\t\tBINARY SEARCH")

        search = input("Enter the ID code of the person you are looking for: ")

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != iD[guess]:

            if search < iD[guess]:

                max = guess - 1
                
            else:

                min = guess + 1

            guess = int((min + max) /2)
            
        if search == iD[guess]:
                
            print("\t\tYour BINARY SEARCH results for", search,": ")

            print("\n{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}\n".format("ID", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))    
            print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}".format(iD[guess], lastName[guess], firstName[guess], age[guess], allegiance[guess]))
            answer = repeat()
            
        else:
            print("\t\tYour BINARY SEARCH results for", search," could NOT be found. ")
            answer = repeat()
    
    if choice == "3":

        print("\n\t\tSEQUENTIAL SEARCH")
  
        search = input("Enter the full lastname of the person/people you want to search for: ").title()
        found = []

        for i in range(0, records):

            if search == lastName[i]:
                found.append(i)
            
    
        if len(found) > 0:
            print("\t\tYour SEQUENTIAL SEARCH results for", search,": ")
            print("\n{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}\n".format("ID", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
            for i in range(0, len(found)):

                
                print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}".format(iD[found[i]], lastName[found[i]], firstName[found[i]], age[found[i]], allegiance[found[i]]))
                

        else:
            print("\t\tYour SEQUENTIAL SEARCH results for", search," could NOT be found. ")
        
        answer = repeat()

    if choice == "4":

        print("\n\t\tSEQUENTIAL SEARCH")
  
        search = input("Enter the allegiance of the person/people you want to search for: ").title()
        found = []

        for i in range(0, records):

            if search == allegiance[i]:
                found.append(i)
            
    
        if len(found) > 0:
            print("\t\tYour SEQUENTIAL SEARCH results for", search,": ")
            print("\n{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}\n".format("ID", "LAST NAME", "FIRST NAME", "AGE", "ALLEGIANCE"))
            for i in range(0, len(found)):

                
                print("{0:15}\t{1:15}\t{2:15}\t{3:5}\t{4:20}".format(iD[found[i]], lastName[found[i]], firstName[found[i]], age[found[i]], allegiance[found[i]]))
                

        else:
            print("\t\tYour SEQUENTIAL SEARCH results for", search," could NOT be found. ")
        
        answer = repeat()

    if choice == "5":
        goodbye()
        answer = "n"