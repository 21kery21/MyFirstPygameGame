import random as r
level = 1
#SCREEN
ROWS = 15
COLS = 15
TILE_SIZE = 48
SIDE_PANEL = 220
SCREEN_WIDTH = TILE_SIZE * COLS
SCREEN_HEIGHT = TILE_SIZE * ROWS

FPS = 60
#ANIMATIONS
ANIMATION_STEPS = 8
ANIMATION_STEPS2 = 11
ANIMATION_STEPS3 = 11
ANIMATION_DELAY = 15
ANIMATION_DELAY2 = 20
ANIMATION_DELAY3 = 18
#UNITS LEVELS
TURRET_LEVELS = 4
SNIPER_LEVELS = 4
FREEZE_LEVELS = 4
MAGMA_LEVELS = 3
ACCELERATOR_LEVELS = 3
#COOLDOWNS
SPAWN_COOLDOWN = 500
BOSS_SUPER_COOLDOWN = 2000
#GAME VALUES
HEALTH = 10
MONEY_L = [1000, 1200, 1400]
MONEY = r.choice(MONEY_L)
DIAMONDS = 0
LEVEL_COMPLETE_REWARD = r.randint(level*20 + 100, level*20 + 150)
#UNITS BUY COST
TURRET_COST = 200
SNIPER_COST = 300
FREEZE_COST = 350
MAGMA_COST = 450
ACCELERATOR_COST = 400
#GAME MODE ENEMY BOOSTS
ENEMY_SPEED_GM_BOOST = 1
ENEMY_HEALTH_GM_BOOST = 1
BOSSES_HEALTH_GM_BOOST = 1
BOSS_RANGE = 140
REGENERATION = 0

TOTAL_LEVELS = 15

