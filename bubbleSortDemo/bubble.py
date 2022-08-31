import csv

records = 0

lastname = []
firstname = []
age = []

with open("bubbleSortDemo/GOT_bubble_sort.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        records += 1

        lastname.append(rec[0])
        firstname.append(rec[1])
        age.append(int(rec[2]))

for i in range(0, records):
    print("{0:15}\t{1:15}\t{2:5}".format(lastname[i], firstname[i], age[i]))

answer = "y"

while answer == "y":

    print("\n\tSEARCH OPTIONS")
    print("1. Search for multiples of 1 name [LASTNAME]")
    print("2. Search for unique name [FIRSTNAME]")
    print("3. EXIT")

    choice = input("\nWhat would you like to do? [1-3]: ").lower()

    while choice != "1" and choice != "2" and choice != "3":
        print("\t\t**ERROR** INVALID ENTRY!")
        choice = input("\nWhat would you like to do? [1-3]: ").lower()

    #SEQUENTIAL SEARCH-------------------------------------------------------------------------------------
    if choice == "1":
        
        print("\n\t\tSEQUENTIAL SEARCH")

        search = input("Enter the lastname of the person/people you are looking for: ")
        f = -1

        found = []

        for i in range(0, records):

            if search == lastname[i]:

                found.append(i)
                f = i
        if f >= 0:
            
            print("\t\tYour SEQUENTIAL SEARCH results for", search,": ")

            for i in range(0, len(found)):
                print("{0:15}\t{1:15}\t{2:5}".format(lastname[found[i]], firstname[found[i]], age[found[i]]))
                answer = input("\n\tWould you like to search again? [y/n]: ")
        
        else:
             print("\t\tYour SEQUENTIAL SEARCH results for", search," could NOT be found. ")
             answer = input("\n\tWould you like to search again? [y/n]: ")


    if choice == "2":
    #BUBBLE SORT-------------------------------------------------------------------------------------------
        for i in range(0, records - 1):#outter loop

            print("OUTER LOOP! i = ", i)


            for index in range(0, records - 1):#inner loop

                print("\t INNER LOOP! k = ", index)

                #below if statement determines the sort

                #list used is the list being sorted

                # > is for increasing order, < for decreasing

                if(firstname[index] > firstname[index + 1]):

                    print("\t\t SWAP! ", firstname[index], "<-->", firstname[index + 1])

                    #if above is true, swap places!

                    temp = firstname[index]

                    firstname[index] = firstname[index + 1]

                    firstname[index + 1] = temp

        
                    #swap all other values

                    temp = age[index]

                    age[index] = age[index + 1]

                    age[index + 1] = temp


                    temp = lastname[index]
                    lastname[index] = lastname[index + 1]
                    lastname[index + 1] = temp



    #BINARY SEARCH-----------------------------------------------------------------------------------------
        print("\n\t\tBINARY SEARCH")

        search = input("Enter the firstname of the person you are looking for: ")

        min = 0
        max = records - 1
        guess = int((min + max) / 2)

        while min < max and search != firstname[guess]:

            if search < firstname[guess]:

                max = guess - 1
            
            else:

                min = guess + 1

            guess = int((min + max) /2)
        
        if search == firstname[guess]:
            
            print("\t\tYour BINARY SEARCH results for", search,": ")

            
            print("{0:15}\t{1:15}\t{2:5}".format(lastname[guess], firstname[guess], age[guess]))
            answer = input("\n\tWould you like to search again? [y/n]: ")
        
        else:
            print("\t\tYour BINARY SEARCH results for", search," could NOT be found. ")
            answer = input("\n\tWould you like to search again? [y/n]: ")



    #EXIT--------------------------------------------------------------------------------------------------