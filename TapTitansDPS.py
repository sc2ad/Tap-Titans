import random
import datetime
import pickle
import time
from TapTitansMain import Player
import TapTitansHeroesDB

# DPS MODULE FOR TAP TITANS

heroes = Player.GetHeroes()
i = 1
for item in heroes:
	if i == 2:
		herolvl = item
	else:
		herodps = TapTitansHeroesDB.dict[hero]
HERODPS = 
