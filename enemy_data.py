import random as r
import constants as c

ENEMY_SPAWN_DATA = [
  {
    #1
    "weak": r.randint(12, 15),
    "medium": 0,
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #2
    "weak": r.randint(15, 30),
    "medium": 0,
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #3
    "weak": 0,
    "medium": r.randint(7, 10),
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #4
    "weak": r.randint(15, 20),
    "medium": r.randint(12, 15),
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #5
    "weak": r.randint(12, 15),
    "medium": r.randint(7, 10),
    "strong": 0,
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #6
    "weak": 0,
    "medium": 0,
    "strong": r.randint(7, 10),
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #7
    "weak": 0,
    "medium": r.randint(20, 25),
    "strong": r.randint(5, 7), 
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #8
    "weak": 0,
    "medium": r.randint(25, 30),
    "strong": r.randint(7, 10),
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #9
    "weak": 0,
    "medium": r.randint(25, 30),
    "strong": r.randint(12, 17),
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #10
    "weak": 0,
    "medium": r.randint(12, 15),
    "strong": r.randint(12, 15),
    "elite": 0,
    "boss": 0,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #11
    "weak": 0,
    "medium": 0,
    "strong": 0,
    "elite": r.randint(12, 15),
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #12
    "weak": 0,
    "medium": 0,
    "strong": r.randint(15, 20),
    "elite": r.randint(12, 15),
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #13
    "weak": 0,
    "medium": r.randint(20, 25),
    "strong": r.randint(10, 12),
    "elite": r.randint(7, 10),
    "boss": 0,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #14
    "weak": 0,
    "medium": 0,
    "strong": r.randint(15, 20),
    "elite": r.randint(15, 20),
    "boss": 1,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #15
    "weak": 0,
    "medium": 0,
    "strong": r.randint(20, 25),
    "elite": r.randint(20, 25),
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 1
  }
]



ENEMY_DATA = {
    "weak": {         
    "health": 10,                             #Health amount
    "speed": 2,                               #Speed of movement
    "cost": r.randint(7, 10),                  #Kill reward (coins)
    "unfreeznes": 1,                          #Freezing protection (1 - none, 0.8 - 20% (1 - 0.8 = 0.2 = 20%) freezing protection, 0 - full protection)
    "HP_steal": 1,                            #Amount of HP what will be stealed after the end of way  
    "weights": [0.85, 0.1, 0.03, 0.02],
    "DMND_BONUS": [0, 1]
  },
    "medium": {
    "health": 15,
    "speed": 3,
    "cost": r.randint(12, 15),
    "unfreeznes": 1,
    "HP_steal": 1,
    "weights": [0.75, 0.15, 0.05, 0.05],
    "DMND_BONUS": [0, 1]
  },
    "strong": {
    "health": 25,
    "speed": 4,
    "cost": r.randint(20, 24),
    "unfreeznes": r.randint(7, 9) * 0.1,
    "HP_steal": 1,
    "weights": [0.75, 0.15, 0.05, 0.05],
    "DMND_BONUS": [0, 1]
  },
    "elite": {
    "health": 50,
    "speed": 1.7,
    "cost": r.randint(25, 30),
    "unfreeznes": r.randint(7, 9) * 0.1,
    "HP_steal": 2,
    "weights": [0.7, 0.2, 0.05, 0.05],
    "DMND_BONUS": [0, 1]
  },
    "boss": {
    "health": 150,
    "speed": 2,
    "cost": 150,
    "unfreeznes": 0,
    "HP_steal": 3,
    "weights": [0, 0.6, 0.3, 0.1],
    "DMND_BONUS": [1, 2]
  },
    "SP_boss": {
    "health": 300,
    "speed": 3,
    "cost": 300,
    "unfreeznes": r.randint(2, 3) * 0.1,
    "HP_steal": 5,
    "weights": [0, 0.5, 0.3, 0.2],
    "DMND_BONUS": [2, 3]
},
    "MG_boss": {
    "health": 0,
    "speed": 1,
    "cost": 1000,
    "unfreeznes": 0,
    "HP_steal": 10,
    "weights": [0, 0, 0, 1],
    "DMND_BONUS": [3, 3]
}}

