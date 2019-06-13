#mightLike by Kristian, Darius, Shandrika, Mariana, and Eric

from uInpData import *

print("""In this program, you will first be asked for a song and
different elements about it. BLAHBLAHBLAHBLAH.
When you're ready, hit 'return' to start.""")
input()

def run_quest (var, que):
    var = input(que)
    print("")
    global inp
    inp = var

#user input
run_quest(uTi, uTiQ)
uTi = inp
run_quest(uCr, uCrQ)
uCr = inp
run_quest(uPer, uPerQ)
uPer = inp
run_quest(uLang, uLangQ)
uLang = inp
run_quest(uDate, uDateQ)
uDate = inp
run_quest(uGen, uGenQ)
uGen = inp
run_quest(uSubG, uSubGQ)
uSubG = inp
run_quest(uTop, uTopQ)
uTop = inp
run_quest(uMood, uMoodQ)
uMood = inp
run_quest(uDI, uDIQ)
uDI = inp
run_quest(uISk, uISkQ)
uISk = inp
run_quest(uLy, uLyQ)
uLy = inp
run_quest(uVo, uVoQ)
uVo = inp
run_quest(uMel, uMelQ)
uMel = inp
run_quest(uRhy, uRhyQ)
uRhy = inp
run_quest(uDDR, uDDRQ)
uDDR = inp
run_quest(uTpo, uTpoQ)
uTpo = inp

print(uTi, uCr, uPer, uLang, uDate, uGen, uSubG, uTop, uMood, uDI, uISk,
      uLy, uVo, uMel, uRhy, uDDR, uTpo)

#algorithm
from algorithumML import *

#graphics
from graphicsML import *
