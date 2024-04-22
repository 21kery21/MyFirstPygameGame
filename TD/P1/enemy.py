import pygame as pg
from pygame.math import Vector2
import math
import constants as c
import random as r
from enemy_data import ENEMY_DATA
from freeze import *

diamond_drop = [0, 1, 2, 3]


class Enemy(pg.sprite.Sprite):
  def __init__(self, enemy_type, waypoints, images):
    pg.sprite.Sprite.__init__(self)
    self.waypoints = waypoints
    self.pos = Vector2(self.waypoints[0])
    self.target_waypoint = 1
    self.health = ENEMY_DATA.get(enemy_type)["health"]
    self.speed = ENEMY_DATA.get(enemy_type)["speed"]
    self.org_speed = self.speed
    self.cost = ENEMY_DATA.get(enemy_type)["cost"]
    self.weights = ENEMY_DATA.get(enemy_type)["weights"]
    self.dmnd_bonus = ENEMY_DATA.get(enemy_type)["DMND_BONUS"]
    self.dmnd_cost = (r.choices(diamond_drop, weights=self.weights, k=1)[0] + self.dmnd_bonus[0]) * self.dmnd_bonus[1]
    self.unfreeznes = ENEMY_DATA.get(enemy_type)["unfreeznes"]
    self.angle = 0
    self.freezing = 1
    self.original_image = images.get(enemy_type)
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos
    self.max_health = self.health
    self.HP_steal = ENEMY_DATA.get(enemy_type)["HP_steal"]
    self.nearest_wayp = None
    self.movement = Vector2(0, 0)
    self.target = Vector2(0, 0)
    self.on_fire = False
    self.last_updt = pg.time.get_ticks()
    self.HP_boosted = 0

    self.range = c.BOSS_RANGE
    self.range_image = pg.Surface((self.range * 2, self.range * 2))
    self.range_image.fill((0,0,0))
    self.range_image.set_colorkey((0,0,0))
    pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
    self.range_image.set_alpha(100)
    self.range_rect = self.range_image.get_rect()
    self.range_rect.center = self.rect.center
    self.target_w = None

  def update(self, world, turret_group, sniper_group, freeze_group, magma_group, accelerator_group, screen):
    self.move(world)
    self.rotate()
    self.check_alive(world)
    if pg.time.get_ticks() - self.last_updt > 1000:
      self.update_properties()
      self.last_updt = pg.time.get_ticks()
    if self.cost == 300:
      self.find_nearest_wayp()
    if self.cost == 1000:
        self.range_rect.center = self.rect.center
        self.cheak_weapons(turret_group, sniper_group, freeze_group, magma_group, accelerator_group)

  def move(self, world):
    #define a target waypoint
    if self.target_waypoint < len(self.waypoints):
      self.target = Vector2(self.waypoints[self.target_waypoint])
      self.movement = self.target - self.pos
    else:
      #enemy has reached the end of the path
      self.kill()
      world.health -= self.HP_steal
      world.missed_enemies += 1

    #calculate distance to target
    dist = self.movement.length()
    #check if remaining distance is greater than the enemy speed
    if dist >= (self.speed * world.game_speed):
      self.pos += self.movement.normalize() * ( world.game_speed * (self.speed / self.freezing))
    else:
      if dist != 0:
        self.pos += self.movement.normalize() * dist
      self.target_waypoint += 1

  def rotate(self):
    #calculate distance to next waypoint
    dist = self.target - self.pos
    #use distance to calculate angle
    self.angle = math.degrees(math.atan2(-dist[1], dist[0]))
    #rotate image and update rectangle
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.rect = self.image.get_rect()
    self.rect.center = self.pos

  def check_alive(self, world):
    if self.health <= 0:
      world.killed_enemies += 1
      world.money += self.cost
      world.diamonds += self.dmnd_cost
      self.kill()
      


  def draw_health_bar(self, screen):
    health_bar_width = int(self.health / self.max_health * self.rect.width * 0.5)
    health_bar_height = 5
    health_bar_color = (255, 0, 0)
    health_bar_border_color = (0, 0, 0)
    health_bar_x = self.rect.centerx - self.rect.width // 4
    health_bar_y = self.rect.top - health_bar_height - 5
    health_bar_border_rect = pg.Rect(health_bar_x - 1, health_bar_y - 1, self.rect.width * 0.5 + 2, health_bar_height + 2)
    pg.draw.rect(screen, health_bar_border_color, health_bar_border_rect)
    health_bar_rect = pg.Rect(health_bar_x, health_bar_y, health_bar_width, health_bar_height)
    pg.draw.rect(screen, health_bar_color, health_bar_rect)

  def draw(self, screen):
    screen.blit(self.image, self.rect)
    if self.cost == 1000:
      screen.blit(self.range_image, self.range_rect)

  def find_nearest_wayp(self):
    if self.cost == 300:
        self.nearest_wayp = None
        min_dist = float('inf')
        for waypoint in self.waypoints:
            dist = math.dist(self.pos, waypoint)
            if dist < min_dist:
                min_dist = dist
                self.nearest_wayp = waypoint
        return self.nearest_wayp
    
  def cheak_weapons(self, turret_group, sniper_group, freeze_group, magma_group, accelerator_group):
    if self.cost == 1000:
      for turret in turret_group:
        self.target_w = turret
        dist = ((turret.rect.centerx - self.rect.centerx) ** 2 + (turret.rect.centery - self.rect.centery) ** 2) ** 0.5
        if dist <= self.range:
          self.target_w.range = self.target_w.org_range - self.target_w.org_range * 0.3
        else:
          self.target_w.range = self.target_w.org_range

      for sniper in sniper_group:
        self.target_w = sniper
        dist = ((sniper.rect.centerx - self.rect.centerx) ** 2 + (sniper.rect.centery - self.rect.centery) ** 2) ** 0.5
        if dist <= self.range:
          self.target_w.range = self.target_w.org_range - self.target_w.org_range * 0.4
        else:
          self.target_w.range = self.target_w.org_range

      for freeze in freeze_group:
        self.target_w = freeze
        dist = ((freeze.rect.centerx - self.rect.centerx) ** 2 + (freeze.rect.centery - self.rect.centery) ** 2) ** 0.5
        if dist <= self.range:
          self.target_w.range = self.target_w.org_range - self.target_w.org_range * 0.25
        else:
          self.target_w.range = self.target_w.org_range

      for magma in magma_group:
        self.target_w = magma
        dist = ((magma.rect.centerx - self.rect.centerx) ** 2 + (magma.rect.centery - self.rect.centery) ** 2) ** 0.5
        if dist <= self.range:
          self.target_w.range = self.target_w.org_range - self.target_w.org_range * 0.25
        else:
          self.target_w.range = self.target_w.org_range

      for accelerator in accelerator_group:
        self.target_w = accelerator
        dist = ((accelerator.rect.centerx - self.rect.centerx) ** 2 + (accelerator.rect.centery - self.rect.centery) ** 2) ** 0.5
        if dist <= self.range:
          self.target_w.range = self.target_w.org_range - self.target_w.org_range * 0.25
        else:
          self.target_w.range = self.target_w.org_range


  def update_properties(self):
    if self.HP_boosted == 0:
      if self.cost <= 24:
        self.HP_boosted += 1
        self.max_health = self.max_health + c.ENEMY_HEALTH_GM_BOOST
        self.health = self.max_health
        self.speed = self.org_speed * c.ENEMY_SPEED_GM_BOOST
      elif 25 <= self.cost <= 30:
        self.HP_boosted += 1
        self.max_health = self.max_health + 5*c.ENEMY_HEALTH_GM_BOOST
        self.health = self.max_health
        self.speed = self.org_speed * c.ENEMY_SPEED_GM_BOOST
      elif self.cost == 150 or self.cost == 300:
        self.HP_boosted += 1
        self.max_health = self.max_health + c.BOSSES_HEALTH_GM_BOOST
        self.health = self.max_health
        self.speed = self.org_speed * c.ENEMY_SPEED_GM_BOOST
      elif self.cost == 1000:
        self.HP_boosted += 1
        self.max_health = self.max_health + 4*c.BOSSES_HEALTH_GM_BOOST
        self.health = self.max_health
        self.range = c.BOSS_RANGE
        self.speed = self.org_speed * c.ENEMY_SPEED_GM_BOOST
    if self.health < self.max_health: 
      self.health = self.health + c.REGENERATION