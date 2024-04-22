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
    "weak": r.randint(25, 30),
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
    "medium": r.randint(10, 12),
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #4
    "weak": r.randint(25, 35),
    "medium": r.randint(12, 15),
    "strong": 0,
    "elite": 0,
    "boss": 0,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #5
    "weak": r.randint(7, 10),
    "medium": r.randint(3, 5),
    "strong": 0,
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #6
    "weak": r.randint(10, 15),
    "medium": r.randint(7, 10),
    "strong": r.randint(3, 5),
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #7
    "weak": r.randint(17, 25),
    "medium": r.randint(15, 20),
    "strong": r.randint(5, 7),
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #8
    "weak": r.randint(10, 12),
    "medium": r.randint(12, 15),
    "strong": r.randint(5, 7),
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #9
    "weak": r.randint(12, 15),
    "medium": r.randint(12, 15),
    "strong": r.randint(7, 10),
    "elite": 0,
    "boss": 1,
    "SP_boss": 0,
    "MG_boss": 0
  },
  {
    #10
    "weak": r.randint(20, 30),
    "medium": r.randint(15, 25),
    "strong": r.randint(5, 7),
    "elite": 0,
    "boss": 0,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #11
    "weak": r.randint(5, 15),
    "medium": r.randint(7, 12),
    "strong": r.randint(5, 7),
    "elite": r.randint(3, 5),
    "boss": 1,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #12
    "weak": r.randint(5, 15),
    "medium": r.randint(7, 12),
    "strong": r.randint(5, 7),
    "elite": r.randint(3, 5),
    "boss": 2,
    "SP_boss": 1,
    "MG_boss": 0
  },
  {
    #13
    "weak": 20,
    "medium": 0,
    "strong": r.randint(7, 12),
    "elite": r.randint(3, 5),
    "boss": 1,
    "SP_boss": 2,
    "MG_boss": 0
  },
  {
    #14
    "weak": 15,
    "medium": 15,
    "strong": r.randint(15, 20),
    "elite": r.randint(10, 12),
    "boss": 2,
    "SP_boss": 2,
    "MG_boss": 0
  },
  {
    #15
    "weak": 0,
    "medium": 0,
    "strong": r.randint(15, 25),
    "elite": r.randint(12, 15),
    "boss": 1,
    "SP_boss": 1,
    "MG_boss": 1
  }
]



ENEMY_DATA = {
    "weak": {         
    "health": 10,                             #Health amount
    "speed": 2,                               #Speed of movement
    "cost": r.randint(4, 5),                  #Kill reward (coins)
    "unfreeznes": 1,                          #Freezing protection (1 - none, 0.8 - 20% (1 - 0.8 = 0.2 = 20%) freezing protection, 0 - full protection)
    "HP_steal": 1,                            #Amount of HP what will be stealed after the end of way  
    "weights": [0.8, 0.1, 0.07, 0.03],
    "DMND_BONUS": [0, 1]
  },
    "medium": {
    "health": 15,
    "speed": 3,
    "cost": r.randint(7, 10),
    "unfreeznes": 1,
    "HP_steal": 1,
    "weights": [0.7, 0.15, 0.1, 0.05],
    "DMND_BONUS": [0, 1]
  },
    "strong": {
    "health": 25,
    "speed": 4,
    "cost": r.randint(12, 15),
    "unfreeznes": r.randint(7, 9) * 0.1,
    "HP_steal": 1,
    "weights": [0.6, 0.2, 0.15, 0.05],
    "DMND_BONUS": [0, 1]
  },
    "elite": {
    "health": 50,
    "speed": 1.7,
    "cost": r.randint(20, 25),
    "unfreeznes": r.randint(5, 7) * 0.1,
    "HP_steal": 2,
    "weights": [0.3, 0.4, 0.2, 0.1],
    "DMND_BONUS": [0, 1]
  },
    "boss": {
    "health": 250,
    "speed": 2,
    "cost": 150,
    "unfreeznes": 0,
    "HP_steal": 3,
    "weights": [0, 0.3, 0.3, 0.4],
    "DMND_BONUS": [1, 2]
  },
    "SP_boss": {
    "health": 300,
    "speed": 3,
    "cost": 300,
    "unfreeznes": r.randint(1, 3) * 0.1,
    "HP_steal": 5,
    "weights": [0, 0.1, 0.1, 0.8],
    "DMND_BONUS": [2, 3]
},
    "MG_boss": {
    "health": 0,
    "speed": 1,
    "cost": 1000,
    "unfreeznes": 0,
    "HP_steal": 10,
    "weights": [0, 0, 0, 0],
    "DMND_BONUS": [0, 0]
}}

