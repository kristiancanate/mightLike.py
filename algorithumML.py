# Algorithum for SL
import csv

# Int Variables
slTi = "Purple Emoji"

slCr = "Ty Dolla $ign, J.Cole"

slPer = "Ty Dolla $ign, J.Cole"

slLang = "English"

slDate = "2019"

slGen = "R&B"

slSubG = "Soul"

slTop = "Relationships"

slMood = "Smooth"

slDI = "Drums"


slISK = 5

slLy = 6

slVo = 8

slMel = 7

slRhy = 9

slDDR = 5

slTpo = 4

# create lists
#sList = []
genMat = []

sList = [row for row in csv.reader(open("songLib.tsv", encoding ='utf-8'), delimiter ="\t")]
##
##with open("songLib.tsv", newline = '', encoding = 'utf - 8') as file:
##          for row in csv.reader(file):
##              sList.append(row)

del sList[0]
del sList[0]

for song in range(len(sList)):
    if sList[song][5] == slGen:
        print("*")
        genMat.append(sList[song])
        
        
    




