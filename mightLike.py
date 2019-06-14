#mightLike by Kristian, Darius, Shandrika, Mariana, and Eric

from uInpData import *
isInt = False

print("""In this program, you will first be asked for a song and
the different elements about it. Read each question carefully and 
take your time answering. After you finish answering the questions,
the program will run through a song library and suggest a song
you may like according to the one you entered.
When you're ready, hit 'return' to start.""")
input()

#user input
uTi = input(uTiQ)
print("")
uCr = input(uCrQ)
print("")
uPer = input(uPerQ)
print("")
uLang = input(uLangQ)
print("")
while isInt == False:
      try:
            uDate = int(input(uDateQ))
            if len(str(uDate)) != 4:
                  print("""
That is not a valid year.
Please choose a song ranging from the 1900-2019.
""")
            elif 2019 < uDate < 1900:
                  print("""
Please choose a song ranging from the 1900-2019.
""")
            else:
                  print("")
                  isInt = True
      except ValueError:
            print("""
That was not an integer.
""")
isInt = False
uGen = input(uGenQ)
print("")
uSubG = input(uSubGQ)
print("")
uTop = input(uTopQ)
print("")
uMood = input(uMoodQ)
print("")
uDI = input(uDIQ)
print("")
uISk = int(input(uISkQ))
print("")
uLy = int(input(uLyQ))
print("")
uVo = int(input(uVoQ))
print("")
uMel = int(input(uMelQ))
print("")
uRhy = int(input(uRhyQ))
print("")
uDDR = int(input(uDDRQ))
print("")
uTpo = int(input(uTpoQ))
print("")

print(uTi, uCr, uPer, uLang, uDate, uGen, uSubG, uTop, uMood, uDI, uISk,
      uLy, uVo, uMel, uRhy, uDDR, uTpo)

#algorithm
from algorithumML import *

#graphics
from graphicsML import *
