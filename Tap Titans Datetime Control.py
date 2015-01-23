import random
import pickle
import datetime
def ReturnLastDate():
    try:
        lasttime = open("LastPlayed.dtf", "r")
    except:
        lasttimefile = open("LastPlayed.dtf", "w")
        lasttimefile.close()
        lasttime = open("LastPlayed.dtf", "r")
    return lasttime.readline()
if ReturnLastDate() != "":
    
