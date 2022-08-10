import csv

#create empty lists
lastname = []
firstname = []
test1 = []
test2 = []
test3 = []

#hand populate lists
teacher = ["KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT", "KT"]

for i in range(0, len(teacher)):
    print(teacher[i])

records = 0

with open("ListReview/listPractice1.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        lastname.append(rec[1])
        firstname.append(rec[0])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

print("Records in file: {}\n".format(records))

print("{:10}\t{:10}\t{}\t{}\t{}".format("FIRSTNAME", "LASTNAME", "TEST 1", "TEST 2", "TEST 3"))
for i in range(0, records):

    print("{:10}\t{:10}\t{}\t{}\t{}".format(firstname[i], lastname[i], test1[i], test2[i], test3[i]))

print("\n")

className = []
stars = []
for i in range(0, len(firstname)):

    className.append("C++")

    star_add = ""

    if test1[i] >= 85:
        star_add += "*"
    if test2[i] >= 85:
        star_add += "*"
    if test3[i] >= 85:
        star_add += "*"


    stars.append(star_add)

print("\t\t{:10}\t{:10}\t{}\t{}\t{}\t{}".format("FIRSTNAME", "LASTNAME", "TEST 1", "TEST 2", "TEST 3", "STARS"))
for i in range(0, records):

    print("CLASS: {}\t{:10}\t{:10}\t{}\t{}\t{}\t{}".format(className[i], firstname[i], lastname[i], test1[i], test2[i], test3[i], stars[i]))