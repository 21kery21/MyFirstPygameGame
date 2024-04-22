import pygame as pg                               #*import pygame
import json                                       #*import json
from enemy import Enemy                           #*import class Enemy from enemy.py
from world import World                           #*import class World from world.py
from turret import Turret                         #*import class Turret from turret.py
from sniper import Sniper                         #*import class Sniper from sniper.py
from freeze import Freeze                         #*import class Freeze from freeze.py
from magma import Magma                           #*import class Magma from magma.py
from accelerator import Accelerator               #*import class Accelerator from accelerator.py
from button import Button                         #*import class Button from button.py
from turret_data import TURRET_DATA               #*import turret properties from turret_data,py
from sniper_data import SNIPER_DATA               #*import sniper properties from sniper_data.py
from freeze_data import FREEZE_DATA               #*import freeze properties from freeze_data.py
from magma_data import MAGMA_DATA                 #*import magma properties from magma_data.py
from accelerator_data import ACCELERATOR_DATA     #*import accelerator properties from accelerator_data.py
import enemy_data as e_d                          #*import enemy properties from enemy_data.py
import constants as c                             #*import constans from constans.py
import random as r                                #*import random

#initialise pygame
pg.init()

#create clock
clock = pg.time.Clock()

#create game window
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

#^game variables############################################
game_over = False
game_outcome = 0  # -1 is loss & 1 is win
level_started = False
last_enemy_spawn = pg.time.get_ticks()
last_minion_spawn = pg.time.get_ticks()
placing_turrets = False
placing_snipers = False
placing_freezs = False
placing_magmas = False
placing_accelerators = False
selected_turret = None
selected_sniper = None
selected_freeze = None
selected_magma = None
selected_accelerator = None
NFT = {}
enemy_types = ["weak", "medium", "strong"]
show_buy_meny_rect = False
show_buy_meny_exit = False
show_swap_meny_rect = False
show_swap_meny_exit = False
show_skills_meny_rect = False
show_skills_meny_exit = False
show_gm_meny_rect = False
show_gm_meny_exit = False
show_ez = True
show_av = True
show_df = True
show_add_butt = False
show_deadd_butt = True
show_IIadd_butt = False
show_IIdeadd_butt = True
Hardcore = False
cheakunits = 0
#^game variables############################################
#!load images###############################################
#map
map_image = pg.image.load('P1/levels/level.png').convert_alpha()
#turret spritesheets
turret_spritesheets = []
for x in range(1, c.TURRET_LEVELS + 1):
  turret_sheet = pg.image.load(f'P1/assets/images/turrets/turret_{x}.png').convert_alpha()
  turret_spritesheets.append(turret_sheet)
#sniper spritesheets
sniper_spritesheets = []
for x in range (1, c.SNIPER_LEVELS + 1):
  sniper_sheet = pg.image.load(f'P1/assets/images/sniper_guns/sniper_gun_{x}.png').convert_alpha()
  sniper_spritesheets.append(sniper_sheet)
#freeze spritesheets
freeze_spritesheets = []
for x in range (1, c.FREEZE_LEVELS + 1):
  freeze_sheet = pg.image.load(f'P1/assets/images/freeze_guns/freeze_gun_{x}.png').convert_alpha()
  freeze_spritesheets.append(freeze_sheet)
#magma images
magma_images = []
for x in range (1, c.MAGMA_LEVELS + 1):
  magma_image = pg.image.load(f'P1/assets/images/magma_towers/magma_tower_{x}.png').convert_alpha()
  magma_images.append(magma_image)
#accelerator images
accelerator_images = []
for x in range (1, c.ACCELERATOR_LEVELS + 1):
  accelerator_image = pg.image.load(f'P1/assets/images/accelerators/accelerator_{x}.png').convert_alpha()
  accelerator_images.append(accelerator_image)
#individual weapon image for mouse cursor
cursor_turret = pg.image.load('P1/assets/images/turrets/cursor_turret.png').convert_alpha()
cursor_sniper = pg.image.load('P1/assets/images/sniper_guns/cursor_sniper_gun.png').convert_alpha()
cursor_freeze = pg.image.load('P1/assets/images/freeze_guns/cursor_freeze.png').convert_alpha()
cursor_magma = pg.image.load('P1/assets/images/magma_towers/magma_tower_1.png').convert_alpha()
cursor_accelerator = pg.image.load('P1/assets/images/accelerators/accelerator_1.png').convert_alpha()
#enemies
enemy_images = {
  "weak": pg.image.load('P1/assets/images/enemies/enemy_1.png').convert_alpha(),
  "medium": pg.image.load('P1/assets/images/enemies/enemy_2.png').convert_alpha(),
  "strong": pg.image.load('P1/assets/images/enemies/enemy_3.png').convert_alpha(),
  "elite": pg.image.load('P1/assets/images/enemies/enemy_4.png').convert_alpha(),
  "boss": pg.image.load('P1/assets/images/enemies/boss.png').convert_alpha(),
  "SP_boss": pg.image.load('P1/assets/images/enemies/SP_boss.png').convert_alpha(),
  "MG_boss": pg.image.load('P1/assets/images/enemies/MG_boss.png').convert_alpha()
}
#buttons
buy_menu_image = pg.image.load('P1/assets/images/buttons/buy_menu.png').convert_alpha()
swap_menu_image = pg.image.load('P1/assets/images/buttons/swap_menu.png').convert_alpha()
exit_image = pg.image.load('P1/assets/images/gui/exit.png').convert_alpha()
buy_image = pg.image.load('P1/assets/images/buttons/buy.png').convert_alpha()
skills_menu_image = pg.image.load('P1/assets/images/buttons/skills_menu.png').convert_alpha()
cancel_image = pg.image.load('P1/assets/images/buttons/cancel.png').convert_alpha()
upgrade_image = pg.image.load('P1/assets/images/buttons/upgrade.png').convert_alpha()
swap_image = pg.image.load('P1/assets/images/buttons/swap.png').convert_alpha()
use_image = pg.image.load('P1/assets/images/buttons/use.png').convert_alpha()
select_image = pg.image.load('P1/assets/images/buttons/select.png').convert_alpha()
GM_menu_image = pg.image.load('P1/assets/images/buttons/GM_menu.png').convert_alpha()
add_image = pg.image.load('P1/assets/images/buttons/add.png').convert_alpha()
deadd_image = pg.image.load('P1/assets/images/buttons/deadd.png').convert_alpha()

begin_image = pg.image.load('P1/assets/images/buttons/begin.png').convert_alpha()
restart_image = pg.image.load('P1/assets/images/buttons/restart.png').convert_alpha()
fast_forward_image = pg.image.load('P1/assets/images/buttons/fast_forward.png').convert_alpha()
#gui
heart_image = pg.image.load("P1/assets/images/gui/heart.png").convert_alpha()
coin_image = pg.image.load("P1/assets/images/gui/coin.png").convert_alpha()
fire_image = pg.image.load("P1/assets/images/gui/fire.png").convert_alpha()
arrow_image = pg.image.load("P1/assets/images/gui/arrow.png").convert_alpha()
diamond_image = pg.image.load("P1/assets/images/gui/diamond.png").convert_alpha()
#info
turret_info_image = pg.image.load("P1/assets/images/gui/turret_info.png").convert_alpha()
sniper_info_image = pg.image.load("P1/assets/images/gui/sniper_info.png").convert_alpha()
freeze_info_image = pg.image.load("P1/assets/images/gui/freeze_info.png").convert_alpha()
magma_info_image = pg.image.load("P1/assets/images/gui/magma_info.png").convert_alpha()
accelerator_info_image = pg.image.load("P1/assets/images/gui/accelerator_info.png").convert_alpha()
#!load images###############################################

#load json data for level
with open('P1/levels/level.tmj') as file:
  world_data = json.load(file)

#load fonts for displaying text on the screen
text_font = pg.font.SysFont("Consolas", 24, bold = True)
upgrd_cost_font = pg.font.SysFont("Consolas", 10, bold = True)
Ifont = pg.font.SysFont("Consolas", 16, bold = True)
large_font = pg.font.SysFont("Consolas", 36)
S_font = pg.font.SysFont("Consolas", 56, bold = True)

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
  lines = text.split('\n')
  y_offset = 0
  for line in lines:
    img = font.render(line, True, text_col)
    screen.blit(img, (x, y + y_offset))
    y_offset += font.get_height()

def display_data():
  #draw panel
  pg.draw.rect(screen, "lightcoral", (c.SCREEN_WIDTH, 0, c.SIDE_PANEL, c.SCREEN_HEIGHT))
  #display data
  draw_text("LEVEL: " + str(world.level), text_font, "grey100", c.SCREEN_WIDTH + 10, 15)
  screen.blit(heart_image, (c.SCREEN_WIDTH + 145, 10))
  draw_text(str(world.health), text_font, "grey100", c.SCREEN_WIDTH + 180, 15)
  screen.blit(coin_image, (c.SCREEN_WIDTH + 20, 50))
  draw_text(str(world.money).split('.')[0], text_font, "grey100", c.SCREEN_WIDTH + 55, 55)
  screen.blit(diamond_image, (c.SCREEN_WIDTH + 140, 50))
  draw_text(str(world.diamonds), text_font, "grey100", c.SCREEN_WIDTH + 175, 55)



  
#&Create weapons functions###########################################
def create_turret(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  #calculate the sequential number of the tile
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  #check if that tile is grass
  if world.tile_map[mouse_tile_num] == 7:
    if (mouse_tile_x, mouse_tile_y) not in NFT:
      new_turret = Turret(turret_spritesheets, mouse_tile_x, mouse_tile_y)
      turret_group.add(new_turret)
      #deduct cost of turret
      world.money -= c.TURRET_COST
      global cheakunits
      cheakunits += 1
      NFT[(mouse_tile_x, mouse_tile_y)] = "nft"

def create_sniper(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  if world.tile_map[mouse_tile_num] == 7:
    if (mouse_tile_x, mouse_tile_y) not in NFT:
      new_sniper = Sniper(sniper_spritesheets, mouse_tile_x, mouse_tile_y)
      sniper_group.add(new_sniper)
      world.money -= c.SNIPER_COST
      global cheakunits
      cheakunits += 1
      NFT[(mouse_tile_x, mouse_tile_y)] = "nft"

def create_freeze(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  if world.tile_map[mouse_tile_num] == 7:
    if (mouse_tile_x, mouse_tile_y) not in NFT:
      new_freeze = Freeze(freeze_spritesheets, mouse_tile_x, mouse_tile_y)
      freeze_group.add(new_freeze)
      world.money -= c.FREEZE_COST
      global cheakunits
      cheakunits += 1
      NFT[(mouse_tile_x, mouse_tile_y)] = "nft"

def create_magma(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  if world.tile_map[mouse_tile_num] == 7:
    if (mouse_tile_x, mouse_tile_y) not in NFT:
      new_magma = Magma(magma_images, mouse_tile_x, mouse_tile_y)
      magma_group.add(new_magma)
      world.money -= c.MAGMA_COST
      global cheakunits
      cheakunits += 1
      NFT[(mouse_tile_x, mouse_tile_y)] = "nft"

def create_accelerator(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  if world.tile_map[mouse_tile_num] == 7:
    if (mouse_tile_x, mouse_tile_y) not in NFT:
      new_accelerator = Accelerator(accelerator_images, mouse_tile_x, mouse_tile_y)
      accelerator_group.add(new_accelerator)
      world.money -= c.ACCELERATOR_COST
      global cheakunits
      cheakunits += 1
      NFT[(mouse_tile_x, mouse_tile_y)] = "nft"
#&Create weapons functions###########################################
#todo#select weapons functions ######################################
def select_turret(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for turret in turret_group:
    if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
      return turret
    
def select_sniper(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for sniper in sniper_group:
    if (mouse_tile_x, mouse_tile_y) == (sniper.tile_x, sniper.tile_y):
      return sniper
    
def select_freeze(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for freeze in freeze_group:
    if (mouse_tile_x, mouse_tile_y) == (freeze.tile_x, freeze.tile_y):
      return freeze
    
def select_magma(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for magma in magma_group:
    if (mouse_tile_x, mouse_tile_y) == (magma.tile_x, magma.tile_y):
      return magma

def select_accelerator(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  for accelerator in accelerator_group:
    if (mouse_tile_x, mouse_tile_y) == (accelerator.tile_x, accelerator.tile_y):
      return accelerator
#unselecting weapons
def clear_selection():
  for turret in turret_group:
    turret.selected = False
  for sniper in sniper_group:
    sniper.selected = False
  for freeze in freeze_group:
    freeze.selected = False
  for magma in magma_group:
    magma.selected = False
  for accelerator in accelerator_group:
    accelerator.selected = False
#todo#select weapons functions ######################################
#create world
world = World(world_data, map_image)
world.process_data()
world.process_enemies()

#create groups
enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()
sniper_group = pg.sprite.Group()
freeze_group = pg.sprite.Group()
magma_group = pg.sprite.Group()
accelerator_group = pg.sprite.Group()

#!create buttons###########################################################
turret_button = Button(c.SCREEN_WIDTH + 15, 197, buy_image, True)
sniper_button = Button(c.SCREEN_WIDTH + 15, 303, buy_image, True)
freeze_button = Button(c.SCREEN_WIDTH + 15, 412, buy_image, True)
magma_button = Button(c.SCREEN_WIDTH + 18, 511, buy_image, True)
accelerator_button = Button(c.SCREEN_WIDTH + 18, 619, buy_image, True)

buy_menu_button = Button(c.SCREEN_WIDTH + 36, 100, buy_menu_image, True)
swap_menu_button = Button(c.SCREEN_WIDTH + 36, 160, swap_menu_image, True)
skills_menu_button = Button(c.SCREEN_WIDTH + 36, 220, skills_menu_image, True)
gm_menu_button = Button(c.SCREEN_WIDTH + 36, 280, GM_menu_image, True)

exit_buy_menu_button = Button(c.SCREEN_WIDTH + 195, 90, exit_image, True)
exit_swap_menu_button = Button(c.SCREEN_WIDTH + 195, 90, exit_image, True)
exit_skills_menu_button = Button(c.SCREEN_WIDTH + 195, 90, exit_image, True)
exit_gm_menu_button = Button(c.SCREEN_WIDTH + 195, 90, exit_image, True)

select_button = Button(c.SCREEN_WIDTH + 15, 165, select_image, True)
IIselect_button = Button(c.SCREEN_WIDTH + 15, 230, select_image, True)
IIIselect_button = Button(c.SCREEN_WIDTH + 15, 305, select_image, True)
add_button = Button(c.SCREEN_WIDTH + 43, 370, add_image, True)
deadd_button = Button(c.SCREEN_WIDTH + 43, 370, deadd_image, True)
IIadd_button = Button(c.SCREEN_WIDTH + 155, 370, add_image, True)
IIdeadd_button = Button(c.SCREEN_WIDTH + 155, 370, deadd_image, True)

use_button = Button(c.SCREEN_WIDTH + 170, 155, use_image, True)
IIuse_button = Button(c.SCREEN_WIDTH + 170, 205, use_image, True)
IIIuse_button = Button(c.SCREEN_WIDTH + 170, 335, use_image, True)
IVuse_button = Button(c.SCREEN_WIDTH + 180, 430, use_image, True)

swap_button = Button(c.SCREEN_WIDTH + 95, 165, swap_image, True)
IIswap_button = Button(c.SCREEN_WIDTH + 95, 255, swap_image, True)
IIIswap_button = Button(c.SCREEN_WIDTH + 95, 345, swap_image, True)
IVswap_button = Button(c.SCREEN_WIDTH + 95, 435, swap_image, True)

cancel_button = Button(c.SCREEN_WIDTH + 43, 197, cancel_image, True)
IIcancel_button = Button(c.SCREEN_WIDTH + 43, 303, cancel_image, True)
IIIcancel_button = Button(c.SCREEN_WIDTH + 43, 412, cancel_image, True)
IVcancel_button = Button(c.SCREEN_WIDTH + 46, 511, cancel_image, True)
Vcancel_button = Button(c.SCREEN_WIDTH + 46 , 619, cancel_image, True)

upgrade_button = Button(c.SCREEN_WIDTH + 43, 197, upgrade_image, True)
IIupgrade_button = Button(c.SCREEN_WIDTH + 43, 303, upgrade_image, True)
IIIupgrade_button = Button(c.SCREEN_WIDTH + 43, 412, upgrade_image, True)
IVupgrade_button = Button(c.SCREEN_WIDTH + 46, 511, upgrade_image, True)
Vupgrade_button = Button(c.SCREEN_WIDTH + 46, 619, upgrade_image, True)

begin_button = Button(c.SCREEN_WIDTH + 26, 660, begin_image, True)
restart_button = Button(310, 300, restart_image, True)
fast_forward_button = Button(c.SCREEN_WIDTH + 19, 660, fast_forward_image, False)
#!create buttons###########################################################

#game loop
run = True
while run:

  clock.tick(c.FPS)

  #########################
  # UPDATING SECTION
  #########################

  BS_SP_CD = c.BOSS_SUPER_COOLDOWN / world.game_speed
  SP_CD = c.SPAWN_COOLDOWN / world.game_speed

  if game_over == False:
    #check if player has lost
    if world.health <= 0:
      game_over = True
      game_outcome = -1 #loss
    #check if player has won
    if world.level > c.TOTAL_LEVELS:
      game_over = True
      game_outcome = 1 #win

    #update groups
    enemy_group.update(world, turret_group, sniper_group, freeze_group, magma_group, accelerator_group, screen)
    turret_group.update(enemy_group, world, screen)
    sniper_group.update(enemy_group, world, screen)
    freeze_group.update(enemy_group, world, screen)
    magma_group.update(enemy_group, world, screen)
    accelerator_group.update(sniper_group, turret_group, freeze_group, magma_group, screen)

    #highlight selected turret
    if selected_turret:
      selected_turret.selected = True

    if selected_sniper:
      selected_sniper.selected = True

    if selected_freeze:
      selected_freeze.selected = True

    if selected_magma:
      selected_magma.selected = True

    if selected_accelerator:
      selected_accelerator.selected = True

  #########################
  # DRAWING SECTION
  #########################

  #draw level
  world.draw(screen)

  #^draw groups#####################
  for enemy in enemy_group:
    enemy.draw(screen)
  for turret in turret_group:
    turret.draw(screen)
  for sniper in sniper_group:
    sniper.draw(screen)
  for freeze in freeze_group:
    freeze.draw(screen)
  for enemy in enemy_group:
    enemy.draw_health_bar(screen)
    if enemy.on_fire == True:
      screen.blit(fire_image, (enemy.rect.left + 7, enemy.rect.top - fire_image.get_height()))
  for magma in magma_group:
    magma.draw(screen)
  for accelerator in accelerator_group:
    accelerator.draw(screen)
  #^draw groups#####################
  display_data()

  if game_over == False:
    #check if the level has been started or not
    if level_started == False:
      if begin_button.draw(screen) and (show_ez == False or show_av == False or show_df == False):
        show_gm_meny_rect = False
        show_gm_meny_exit = False
        level_started = True
    else:
      #fast forward option
      world.game_speed = 1
      if fast_forward_button.draw(screen):
        world.game_speed = 3
      #spawn enemies
      if pg.time.get_ticks() - last_enemy_spawn > SP_CD:
        if world.spawned_enemies - world.spawned_minions < len(world.enemy_list):
          enemy_type = world.enemy_list[world.spawned_enemies - world.spawned_minions]
          enemy = Enemy(enemy_type, world.waypoints, enemy_images)
          enemy_group.add(enemy)
          for enemy in enemy_group:
            enemy.update_properties()
          world.spawned_enemies += 1
          last_enemy_spawn = pg.time.get_ticks()

      if pg.time.get_ticks() - last_minion_spawn > BS_SP_CD:
        for enemy in enemy_group:
          if enemy.cost == 300:
            enemy_type = r.choice(enemy_types)
            nearest_wayp = enemy.find_nearest_wayp()
            new_enemy = Enemy(enemy_type, world.waypoints[world.waypoints.index(nearest_wayp):], enemy_images)
            enemy_group.add(new_enemy)
            world.spawned_minions += 1
            world.spawned_enemies += 1
            print("minik")
            last_minion_spawn = pg.time.get_ticks()
            break

    #check if the wave is finished
    if world.check_level_complete() == True:
      world.money += c.LEVEL_COMPLETE_REWARD
      world.level += 1
      c.level += 1
      level_started = False
      last_enemy_spawn = pg.time.get_ticks()
      world.reset_level()
      world.process_enemies()

    #check player time glitching with coins
    if world.money < 0 and world.health > 0:
      world.money += 100
      world.health -= 1
    #fix minus HP visual bag
    if world.health < 0:
      world.health = 0
    #fix gm menu visual bag after lvl start
    

    #~draw and use buttons####################################################################
    if show_ez == True and show_av == True and show_df == True:
      draw_text("!", S_font, "red", c.SCREEN_WIDTH + 180, 282)
      draw_text("(first select hardness)", upgrd_cost_font, "yellow", c.SCREEN_WIDTH + 40, 663)
    if show_buy_meny_rect == False and show_skills_meny_rect == False and show_swap_meny_rect == False and world.level == 1 and level_started == False:
      if gm_menu_button.draw(screen):
        show_gm_meny_rect = True
        show_gm_meny_exit = True
      
    if show_gm_meny_rect == True:
      pg.draw.rect(screen, "papayawhip", (c.SCREEN_WIDTH + 7, 100, c.SIDE_PANEL - 14, 300), border_radius=10)
      draw_text("----Easiest----", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 105)
      draw_text("Easiest difficulty to familiarize\nyourself with the basic techniques\nof the game (without enemy boosts)", upgrd_cost_font, "yellowgreen", c.SCREEN_WIDTH + 9, 130)
      draw_text("----Average----", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 180)
      draw_text("Default difficulty to play (small\nspeed and health enemy boost)", upgrd_cost_font, "yellowgreen", c.SCREEN_WIDTH + 12, 205)
      draw_text("---Difficult---", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 245)
      draw_text("Default difficulty to play (30%\nspeed and health enemy boost,\nnew enemy ability - autoregen)", upgrd_cost_font, "yellowgreen", c.SCREEN_WIDTH + 12, 270)
      draw_text("---+Addition---", text_font, "lightcoral", c.SCREEN_WIDTH + 10, 320)
      draw_text("More money at\nthe beginning", upgrd_cost_font, "lightcoral", c.SCREEN_WIDTH + 12, 345)
      draw_text("Hardcore (1 HP\nfor all game)", upgrd_cost_font, "lightcoral", c.SCREEN_WIDTH + 122, 345)
      pg.draw.circle(screen, "gainsboro", (c.SCREEN_WIDTH + 164, 384), radius=10.5, width=1)

      



    if show_gm_meny_exit == True:
      if exit_gm_menu_button.draw(screen):
        show_gm_meny_rect = False
        show_gm_meny_exit = False

    if show_gm_meny_rect == True:
      if show_ez == True:
        if select_button.draw(screen):
          c.ENEMY_SPEED_GM_BOOST = 1
          c.ENEMY_HEALTH_GM_BOOST = 0
          c.BOSSES_HEALTH_GM_BOOST = 0
          c.BOSS_RANGE = 140
          c.REGENERATION = 0
          if cheakunits == 0:
            c.MONEY = r.choice(c.MONEY_L)
            world.money = c.MONEY
          show_ez = False
          show_av = True
          show_df = True
      if show_av == True:
        if IIselect_button.draw(screen):
          c.ENEMY_SPEED_GM_BOOST = 1.15
          c.ENEMY_HEALTH_GM_BOOST = 2
          c.BOSSES_HEALTH_GM_BOOST = 25
          c.BOSS_RANGE = 150
          c.REGENERATION = 0
          if cheakunits == 0:
            c.MONEY = r.choice(c.MONEY_L) + 300
            world.money = c.MONEY
          show_ez = True
          show_av = False
          show_df = True
      if show_df == True:
        if IIIselect_button.draw(screen):
          c.ENEMY_SPEED_GM_BOOST = 1.3
          c.ENEMY_HEALTH_GM_BOOST = 3
          c.BOSSES_HEALTH_GM_BOOST = 35
          c.BOSS_RANGE = 160
          c.REGENERATION = 0.5
          if cheakunits == 0:
            c.MONEY = r.choice(c.MONEY_L) + 500
            world.money = c.MONEY
          show_ez = True
          show_av = True
          show_df = False
      if cheakunits == 0 and world.health == c.HEALTH:
        pg.draw.circle(screen, "gainsboro", (c.SCREEN_WIDTH + 52, 384), radius=10.5, width=1)
        if show_add_butt == True:
          if add_button.draw(screen):
            show_add_butt = False
            show_deadd_butt = True
            world.money = c.MONEY
            world.diamonds = c.DIAMONDS
        if show_deadd_butt == True:
          if deadd_button.draw(screen):
            show_deadd_butt = False
            show_add_butt = True
            world.money = 99999
            world.diamonds = 999
      if show_IIadd_butt == True:
        if IIadd_button.draw(screen):
          show_IIadd_butt = False
          show_IIdeadd_butt = True
          Hardcore = False
          c.HEALTH = 10
          world.health = c.HEALTH
      if show_IIdeadd_butt == True:
        if IIdeadd_button.draw(screen):
          show_IIdeadd_butt = False
          show_IIadd_butt = True
          Hardcore = True
          c.HEALTH = 1
          world.health = c.HEALTH



    if show_buy_meny_rect == False and show_swap_meny_rect == False and show_gm_meny_rect == False:
      if skills_menu_button.draw(screen):
        show_skills_meny_rect = True
        show_skills_meny_exit = True

    if show_skills_meny_rect == True:
      pg.draw.rect(screen, "papayawhip", (c.SCREEN_WIDTH + 7, 100, c.SIDE_PANEL - 14, 365), border_radius=10)
      draw_text("-Little-Robber-", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 105)
      draw_text("Takes 10 HP from\nall enemies\non the map", Ifont, "yellowgreen", c.SCREEN_WIDTH + 63, 135)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 19, 130))
      draw_text("20", Ifont, "goldenrod", c.SCREEN_WIDTH + 26, 166)
      draw_text("---SnowStorm---", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 185)
      draw_text("Slows all \nenemies on the\nmap by two times", Ifont, "yellowgreen", c.SCREEN_WIDTH + 63, 215)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 19, 210))
      draw_text("15", Ifont, "goldenrod", c.SCREEN_WIDTH + 26, 246)
      draw_text("---Investment--", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 265)
      draw_text("10% discount on \nall upgrades of \nall weapons \non map", Ifont, "yellowgreen", c.SCREEN_WIDTH + 63, 295)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 19, 290))
      draw_text("15", Ifont, "goldenrod", c.SCREEN_WIDTH + 26, 326)
      draw_text("--AntiStealer--", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 365)
      draw_text("HP steal of each \nenemy on the map \nreduced by 1", Ifont, "yellowgreen", c.SCREEN_WIDTH + 63, 395)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 19, 390))
      draw_text("35", Ifont, "goldenrod", c.SCREEN_WIDTH + 26, 426)

    if show_skills_meny_exit == True:
      if exit_skills_menu_button.draw(screen):
        show_skills_meny_rect = False
        show_skills_meny_exit = False
    if show_skills_meny_rect == True:
      if use_button.draw(screen):
        if world.diamonds >= 20:
          world.diamonds -= 20
          for enemy in enemy_group:
            enemy.health -= 10

      if IIuse_button.draw(screen):
        if world.diamonds >= 15:
          world.diamonds -= 15
          for enemy in enemy_group:
            if enemy.speed > 1:
              enemy.speed = enemy.speed / 2

      if IIIuse_button.draw(screen):
        if world.diamonds >= 15:
          world.diamonds -= 15
          for turret in turret_group:
            turret.upgrade_discount = 0.1
            turret.upgrade_cost = turret.upgrade_cost - turret.upgrade_cost * turret.upgrade_discount
          for sniper in sniper_group:
            sniper.upgrade_discount = 0.1
            sniper.upgrade_cost = sniper.upgrade_cost - sniper.upgrade_cost * sniper.upgrade_discount
          for freeze in freeze_group:
            freeze.upgrade_discount = 0.1
            freeze.upgrade_cost = freeze.upgrade_cost - freeze.upgrade_cost * freeze.upgrade_discount
          for magma in magma_group:
            magma.upgrade_discount = 0.1
            magma.upgrade_cost = magma.upgrade_cost - magma.upgrade_cost * magma.upgrade_discount
          for accelerator in accelerator_group:
            accelerator.upgrade_discount = 0.1
            accelerator.upgrade_cost = accelerator.upgrade_cost - accelerator.upgrade_cost * accelerator.upgrade_discount

      if IVuse_button.draw(screen):
        if world.diamonds >= 35:
          world.diamonds -= 35
          for enemy in enemy_group:
            if enemy.HP_steal >= 1:
              enemy.HP_steal -= 1
    




    if show_buy_meny_rect == False and show_skills_meny_rect == False and show_gm_meny_rect == False:
      if swap_menu_button.draw(screen):
        show_swap_meny_rect = True
        show_swap_meny_exit = True

    if show_swap_meny_rect == True:
      pg.draw.rect(screen, "papayawhip", (c.SCREEN_WIDTH + 7, 100, c.SIDE_PANEL - 14, 365), border_radius=10)
      draw_text("-Coin-to-Heart-", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 105)
      screen.blit(coin_image, (c.SCREEN_WIDTH + 35, 135))
      draw_text("1000", Ifont, "goldenrod", c.SCREEN_WIDTH + 33, 171)
      screen.blit(arrow_image, (c.SCREEN_WIDTH + 83, 140))
      screen.blit(heart_image, (c.SCREEN_WIDTH + 150, 135))
      draw_text("-Heart-to-Coin-", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 195)
      screen.blit(heart_image, (c.SCREEN_WIDTH + 35, 225))
      screen.blit(arrow_image, (c.SCREEN_WIDTH + 83, 230))
      screen.blit(coin_image, (c.SCREEN_WIDTH + 150, 225))
      draw_text("100", Ifont, "goldenrod", c.SCREEN_WIDTH + 152, 261)
      draw_text("-DiMND-to-Coin-", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 285)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 35, 315))
      screen.blit(arrow_image, (c.SCREEN_WIDTH + 83, 320))
      screen.blit(coin_image, (c.SCREEN_WIDTH + 150, 315))
      draw_text("5", Ifont, "goldenrod", c.SCREEN_WIDTH + 161, 351)
      draw_text("-Coin-to-DiMND-", text_font, "lightseagreen", c.SCREEN_WIDTH + 10, 375)
      screen.blit(diamond_image, (c.SCREEN_WIDTH + 150, 405))
      screen.blit(arrow_image, (c.SCREEN_WIDTH + 83, 410))
      screen.blit(coin_image, (c.SCREEN_WIDTH + 35, 405))
      draw_text("50", Ifont, "goldenrod", c.SCREEN_WIDTH + 42, 441)


    if show_swap_meny_exit == True:
      if exit_swap_menu_button.draw(screen):
        show_swap_meny_exit = False
        show_swap_meny_rect = False

    if show_swap_meny_rect == True and Hardcore == False:
      if swap_button.draw(screen):
        if world.money >= 1000:
          world.money -= 1000
          world.health += 1 
    if show_swap_meny_rect == True and world.health >= 2:
      if IIswap_button.draw(screen):
        if world.health >= 2 and level_started == True:
          world.money += 100
          world.health -= 1 
    if show_swap_meny_rect == True:
      if IIIswap_button.draw(screen):
        if world.diamonds >= 1:
          world.money += 5
          world.diamonds -= 1 
    if show_swap_meny_rect == True:
      if IVswap_button.draw(screen):
        if world.money >= 50:
          world.money -= 50
          world.diamonds += 1 
    
    if show_swap_meny_rect == False and show_skills_meny_rect == False and show_gm_meny_rect == False:
      if buy_menu_button.draw(screen):
        show_buy_meny_rect = True
        show_buy_meny_exit = True
    if show_buy_meny_rect == True:
      pg.draw.rect(screen, "papayawhip", (c.SCREEN_WIDTH + 7, 100, c.SIDE_PANEL - 14, 550), border_radius=10)
      draw_text("-----Turret----", text_font, "tomato", c.SCREEN_WIDTH + 10, 105)
      draw_text("-----Sniper----", text_font, "tomato", c.SCREEN_WIDTH + 10, 215)
      draw_text("-----Freeze----", text_font, "tomato", c.SCREEN_WIDTH + 10, 322)
      draw_text("-----Magma-----", text_font, "tomato", c.SCREEN_WIDTH + 10, 429)
      draw_text("--Accelerator--", text_font, "tomato", c.SCREEN_WIDTH + 10, 534)
      pg.draw.rect(screen, "gray", (c.SCREEN_WIDTH + 15, 125, 52, 70), 2, border_radius=3)
      screen.blit(cursor_turret, (c.SCREEN_WIDTH-7, 118))
      screen.blit(turret_info_image, (c.SCREEN_WIDTH + 80, 127))
      draw_text(str(c.TURRET_COST), upgrd_cost_font, "goldenrod", c.SCREEN_WIDTH + 17, 127)
      pg.draw.rect(screen, "gray", (c.SCREEN_WIDTH + 15, 231, 52, 70), 2, border_radius=3)
      screen.blit(cursor_sniper, (c.SCREEN_WIDTH-7, 223))
      screen.blit(sniper_info_image, (c.SCREEN_WIDTH + 80, 240))
      draw_text(str(c.SNIPER_COST), upgrd_cost_font, "goldenrod", c.SCREEN_WIDTH + 17, 233)
      pg.draw.rect(screen, "gray", (c.SCREEN_WIDTH + 15, 340, 52, 70), 2, border_radius=3)
      screen.blit(cursor_freeze, (c.SCREEN_WIDTH-7, 327))
      screen.blit(freeze_info_image, (c.SCREEN_WIDTH + 71, 345))
      draw_text(str(c.FREEZE_COST), upgrd_cost_font, "goldenrod", c.SCREEN_WIDTH + 17, 342)
      pg.draw.rect(screen, "gray", (c.SCREEN_WIDTH + 15, 451, 58, 58), 2, border_radius=3)
      screen.blit(cursor_magma, (c.SCREEN_WIDTH-4, 431))
      screen.blit(magma_info_image, (c.SCREEN_WIDTH + 84, 458))
      draw_text(str(c.MAGMA_COST), upgrd_cost_font, "goldenrod", c.SCREEN_WIDTH + 17, 442)
      pg.draw.rect(screen, "gray", (c.SCREEN_WIDTH + 15, 558, 58, 58), 2, border_radius=3)
      screen.blit(cursor_accelerator, (c.SCREEN_WIDTH-4, 540))
      screen.blit(accelerator_info_image, (c.SCREEN_WIDTH + 84, 561))
      draw_text(str(c.ACCELERATOR_COST), upgrd_cost_font, "goldenrod", c.SCREEN_WIDTH + 17, 549)
    if show_buy_meny_exit == True:
      if exit_buy_menu_button.draw(screen):
        show_buy_meny_rect = False
        show_buy_meny_exit = False
        placing_magmas = False
        placing_snipers = False
        placing_freezs = False
        placing_turrets = False
        placing_accelerators = False
  

    if show_buy_meny_rect == True:
      if freeze_button.draw(screen) and placing_turrets == False and placing_snipers == False and placing_magmas == False and placing_accelerators == False:
        placing_freezs = True
      if placing_freezs == True:
        cursor_rect = cursor_freeze.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(cursor_freeze, cursor_rect)
        if IIIcancel_button.draw(screen):
          placing_freezs = False
      if selected_freeze:
        if selected_freeze.upgrade_level < c.FREEZE_LEVELS:
          if IIIupgrade_button.draw(screen):
            if world.money >= selected_freeze.upgrade_cost:
              selected_freeze.upgrade()
              world.money -= selected_freeze.upgrade_cost
          draw_text("-" + (str(FREEZE_DATA[selected_freeze.upgrade_level].get("upgrade_cost") - FREEZE_DATA[selected_freeze.upgrade_level].get("upgrade_cost")*selected_freeze.upgrade_discount)).split('.')[0], upgrd_cost_font, "red", c.SCREEN_WIDTH + 60, 410)

    if show_buy_meny_rect == True:
      if accelerator_button.draw(screen) and placing_turrets == False and placing_snipers == False and placing_magmas == False and placing_freezs == False:
        placing_accelerators = True
      if placing_accelerators == True:
        cursor_rect = cursor_accelerator.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(cursor_accelerator, cursor_rect)
        if Vcancel_button.draw(screen):
          placing_accelerators = False
      if selected_accelerator:
        if selected_accelerator.upgrade_level < c.ACCELERATOR_LEVELS:
          if Vupgrade_button.draw(screen):
            if world.money >= selected_accelerator.upgrade_cost:
              selected_accelerator.upgrade()
              world.money -= selected_accelerator.upgrade_cost
          draw_text("-" + (str(ACCELERATOR_DATA[selected_accelerator.upgrade_level].get("upgrade_cost") - ACCELERATOR_DATA[selected_accelerator.upgrade_level].get("upgrade_cost")*selected_accelerator.upgrade_discount)).split('.')[0], upgrd_cost_font, "red", c.SCREEN_WIDTH + 63, 617)

    if show_buy_meny_rect == True:
      if sniper_button.draw(screen) and placing_turrets == False and placing_freezs == False and placing_magmas == False and placing_accelerators == False:
        placing_snipers = True
      if placing_snipers == True:
        cursor_rect = cursor_sniper.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(cursor_sniper, cursor_rect)
        if IIcancel_button.draw(screen):
          placing_snipers = False
      if selected_sniper:
        if selected_sniper.upgrade_level < c.SNIPER_LEVELS:
          if IIupgrade_button.draw(screen):
            if world.money >= selected_sniper.upgrade_cost:
              selected_sniper.upgrade()
              world.money -= selected_sniper.upgrade_cost
          draw_text("-" + (str(SNIPER_DATA[selected_sniper.upgrade_level].get("upgrade_cost") - SNIPER_DATA[selected_sniper.upgrade_level].get("upgrade_cost")*selected_sniper.upgrade_discount)).split('.')[0], upgrd_cost_font, "red", c.SCREEN_WIDTH + 60, 300)

    if show_buy_meny_rect == True:
      if magma_button.draw(screen) and placing_turrets == False and placing_freezs == False and placing_snipers == False and placing_accelerators == False:
        placing_magmas = True
      if placing_magmas == True:
        cursor_rect = cursor_magma.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(cursor_magma, cursor_rect)
        if IVcancel_button.draw(screen):
          placing_magmas = False
      if selected_magma:
        if selected_magma.upgrade_level < c.MAGMA_LEVELS:
          if IVupgrade_button.draw(screen):
            if world.money >= selected_magma.upgrade_cost:
              selected_magma.upgrade()
              world.money -= selected_magma.upgrade_cost
          draw_text("-" + (str(MAGMA_DATA[selected_magma.upgrade_level].get("upgrade_cost") - MAGMA_DATA[selected_magma.upgrade_level].get("upgrade_cost")*selected_magma.upgrade_discount)).split('.')[0], upgrd_cost_font, "red", c.SCREEN_WIDTH + 63, 509)

    if show_buy_meny_rect == True:
      if turret_button.draw(screen) and placing_snipers == False and placing_freezs == False and placing_magmas == False and placing_accelerators == False:
        placing_turrets = True
      #if placing turrets then show the cancel button as well
      if placing_turrets == True:
        #show cursor turret
        cursor_rect = cursor_turret.get_rect()
        cursor_pos = pg.mouse.get_pos()
        cursor_rect.center = cursor_pos
        if cursor_pos[0] <= c.SCREEN_WIDTH:
          screen.blit(cursor_turret, cursor_rect)
        if cancel_button.draw(screen):
          placing_turrets = False
      #if a turret is selected then show the upgrade button
      if selected_turret:
        #if a turret can be upgraded then show the upgrade button
        if selected_turret.upgrade_level < c.TURRET_LEVELS:
          #show cost of upgrade and draw the button
          screen.blit(coin_image, (c.SCREEN_WIDTH + 260, 190))
          if upgrade_button.draw(screen):
            if world.money >= selected_turret.upgrade_cost:
              selected_turret.upgrade()
              world.money -= selected_turret.upgrade_cost
          draw_text("-" + (str(TURRET_DATA[selected_turret.upgrade_level].get("upgrade_cost") - TURRET_DATA[selected_turret.upgrade_level].get("upgrade_cost")*selected_turret.upgrade_discount)).split('.')[0], upgrd_cost_font, "red", c.SCREEN_WIDTH + 60, 194)


      

  #~draw buttons####################################################################   

            
  else:
    pg.draw.rect(screen, "dodgerblue", (200, 200, 400, 200), border_radius = 30)
    if game_outcome == -1:
      draw_text("GAME OVER", large_font, "grey0", 310, 230)
    elif game_outcome == 1:
      draw_text("YOU WIN!", large_font, "grey0", 315, 230)
    #restart level
    if restart_button.draw(screen):
      game_over = False
      level_started = False
      placing_turrets = False
      placing_snipers = False
      placing_freezs = False
      placing_magmas = False
      placing_accelerators = False
      selected_turret = None
      selected_sniper = None
      selected_freeze = None
      selected_magma = None
      selected_accelerator = None
      last_enemy_spawn = pg.time.get_ticks()
      last_minion_spawn = pg.time.get_ticks()
      world = World(world_data, map_image)
      world.process_data()
      world.process_enemies()
      #empty groups
      enemy_group.empty()
      turret_group.empty()
      sniper_group.empty()
      freeze_group.empty()
      magma_group.empty()
      accelerator_group.empty()
      NFT = {}
      
  
  #event handler
  for event in pg.event.get():
    #quit program
    if event.type == pg.QUIT:
      run = False
    #mouse click
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pg.mouse.get_pos()
      #check if mouse is on the game area
      if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
        #clear selected turrets, snipers
        selected_turret = None
        selected_sniper = None
        selected_freeze = None
        selected_magma = None
        selected_accelerator = None
        clear_selection()
        if placing_magmas == True and placing_turrets == False and placing_freezs == False and placing_snipers == False and placing_accelerators == False:
          if world.money >= c.MAGMA_COST:
            create_magma(mouse_pos)
        else:
          selected_magma = select_magma(mouse_pos)

        if placing_accelerators == True and placing_turrets == False and placing_freezs == False and placing_snipers == False and placing_magmas == False:
          if world.money >= c.ACCELERATOR_COST:
            create_accelerator(mouse_pos)
        else:
          selected_accelerator = select_accelerator(mouse_pos)

        if placing_snipers == True and placing_turrets == False and placing_freezs == False and placing_magmas == False and placing_accelerators == False:
          if world.money >= c.SNIPER_COST:
            create_sniper(mouse_pos)
        else:
          selected_sniper = select_sniper(mouse_pos)

        if placing_turrets == True and placing_snipers == False and placing_freezs == False and placing_magmas == False and placing_accelerators == False:
          #check if there is enough money for a turret
          if world.money >= c.TURRET_COST:
            create_turret(mouse_pos)
        else:
          selected_turret = select_turret(mouse_pos)

        if placing_freezs == True and placing_snipers == False and placing_turrets == False and placing_magmas == False and placing_accelerators == False:
          if world.money >= c.FREEZE_COST:
            create_freeze(mouse_pos)
        else:
          selected_freeze = select_freeze(mouse_pos)
       
        


  #update display
  pg.display.flip()

pg.quit()