import random
import pickle
import datetime
import TapTitansDPS

LASTPLAYEDDIR = "LastPlayed.dtf"

def ReturnLastDate():
    try:
        lasttime = open(LASTPLAYEDDIR, "r")
    except:
        WriteToFileP(LASTPLAYEDDIR,datetime.datetime.now())
        lasttime = open(LASTPLAYEDDIR, "r")
    then = pickle.load(lasttime)
    lasttime.close()
    return then
def WriteToFileP(path,data):
	file2 = open(path, "w")
	pickle.dump(data,file2)
	file2.close()
def WriteLastDate():
	WriteToFileP(LASTPLAYEDDIR,datetime.datetime.now())
if ReturnLastDate() != "":
    now = datetime.datetime.now()
    then = ReturnLastDate()
    delta = now-then
    print "Days since last play: "+str(delta.days)+"\nHours since last play: "+str(int(delta.seconds/3600))+"\nMinutes since last play: "+str(int(delta.seconds/60))+"\nSeconds since last play: "+str(delta.seconds-int(delta.seconds/3600)-(int(delta.seconds/60)*60))+"\nFlat out time since last play: "+str(delta)
DPS = TapTitansDPS.HERODPS
print "Total DPS Done while you were away: "+str(DPS*delta.seconds)

