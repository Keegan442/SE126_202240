#Midterm Project
#Keegan Preston

#Program Prompt: This program reads a list of metal bands and organizes it by name of the band, year they formed, their country of origin, year they split(if they did), and the style of the band. Then the program takes that information and outputs how many bands are from each country and how many bands are still active. 

#Variable Dictionary:
#records - number of records in file
#amBands - number of american bands
#ukBands - number of UK bands
#swBands - number of swedish bands
#fiBands - number of finnish bands
#poBands - number of polish bands
#noBands - number of norweigen bands
#neBands - number of netherlands bands
#geBands - number of german bands
#frBands - number of french bands
#brBands - number of brazilian bands
#ptBands - number of portugal bands
#auBands - number of australian bands
#stillActive - number of bands still active
#number - order of file
#bandName - name of the band
#numFans - number of fans on website of band
#yrFormed - year the band was formed
#conOrg - country of origin
#yrSplit - year the band split (if they did)
#style - music style of band

#MAIN CODE------------------------------------------------------------------------------------------------------------------------

import csv

records = 0
amBands = 0
ukBands = 0
swBands = 0
fiBands = 0
poBands = 0
noBands = 0
neBands = 0
geBands = 0
frBands = 0
brBands = 0
ptBands = 0
auBands = 0
stillActive = 0

number = []
bandName = []
numFans = []
yrFormed = []
conOrg = []
yrSplit = []
style = []

with open("Midterm/metal_bands_2017.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        records += 1

        number.append(rec[0])
        bandName.append(rec[1])
        numFans.append(int(rec[2]))
        yrFormed.append(rec[3])
        conOrg.append(rec[4])
        yrSplit.append(rec[5])
        style.append(rec[6])
    
print("{0:5}\t {1:15}\t {2:10}\t {3:15}\t {4:10}\t {5:6}\t {6:25}\t".format("#", "BAND NAME", "WEBSITE USERS", "YEAR FORMED", "COUNTRY", "YEAR SPLIT", "STYLE"))
for i in range(0, records):

    if conOrg[i] == "USA":
        amBands += 1
    elif conOrg[i] == "United Kingdom":
        ukBands += 1
    elif conOrg[i] == "Sweden":
        swBands += 1
    elif conOrg[i] == "Finland":
        fiBands += 1
    elif conOrg[i] == "Poland":
        poBands += 1
    elif conOrg[i] == "Norway":
        noBands += 1
    elif conOrg[i] == "The Netherlands":
        neBands += 1
    elif conOrg[i] == "Germany":
        geBands += 1
    elif conOrg[i] == "France":
        frBands += 1
    elif conOrg[i] == "Brazil":
        brBands += 1
    elif conOrg[i] == "Portugal":
        ptBands += 1
    elif conOrg[i] == "Australia":
        auBands += 1
    
    if yrSplit[i] == "-":
        stillActive += 1
    else:
        stillActive += 0

    print("{0:5}\t {1:15}\t {2:10}\t {3:15}\t {4:10}\t {5:6}\t {6:25}\t".format(number[i], bandName[i], numFans[i], yrFormed[i], conOrg[i], yrSplit[i], style[i]))

print("\nThere is {} band(s) from America".format(amBands))
print("There is {} band(s) from The United Kindom".format(ukBands))
print("There is {} band(s) from Sweden".format(swBands))
print("There is {} band(s) from Finland".format(fiBands))
print("There is {} band(s) from Poland".format(poBands))
print("There is {} band(s) from Norway".format(noBands))
print("There is {} band(s) from The Netherlands".format(neBands))
print("There is {} band(s) from Germany".format(geBands))
print("There is {} band(s) from France".format(frBands))
print("There is {} band(s) from Brazil".format(brBands))
print("There is {} band(s) from Portugal".format(poBands))
print("There is {} band(s) from Australia\n".format(auBands))

print("There are {} bands still active\n".format(stillActive))