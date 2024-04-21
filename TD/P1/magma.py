import pygame as pg
import constants as c
from magma_data import MAGMA_DATA


class Magma(pg.sprite.Sprite):
    def __init__(self, images, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE
        self.selected = False
        self.range = MAGMA_DATA[self.upgrade_level-1].get("range")
        self.org_range = MAGMA_DATA[self.upgrade_level-1].get("range")
        self.cooldown = MAGMA_DATA[self.upgrade_level-1].get("cooldown")
        self.org_cooldown = MAGMA_DATA[self.upgrade_level-1].get("cooldown")
        self.upgrade_cost = MAGMA_DATA[self.upgrade_level-1].get("upgrade_cost")
        self.upgrade_discount = 0
        self.last_shot = pg.time.get_ticks()
        self.last_updt = pg.time.get_ticks()
        self.target = None

        self.images = images
        self.image = self.images[self.upgrade_level-1].convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def update(self, enemy_group, world, screen):
        if pg.time.get_ticks() - self.last_updt > 500:
            self.last_updt = pg.time.get_ticks()
            self.range_updt(screen)
        self.load_images()
        if pg.time.get_ticks() - self.last_shot > (self.cooldown / world.game_speed):
            self.last_shot = pg.time.get_ticks()
            self.check_enemies(enemy_group)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.selected:
            screen.blit(self.range_image, self.range_rect)

    def load_images(self):
        self.image = self.images[self.upgrade_level-1].convert_alpha()


    def upgrade(self):
        self.upgrade_level += 1
        self.range = MAGMA_DATA[self.upgrade_level-1].get("range")
        self.org_range = MAGMA_DATA[self.upgrade_level-1].get("range")
        self.cooldown = MAGMA_DATA[self.upgrade_level-1].get("cooldown")
        self.org_cooldown = MAGMA_DATA[self.upgrade_level-1].get("cooldown")
        self.upgrade_cost = MAGMA_DATA[self.upgrade_level-1].get("upgrade_cost") - (MAGMA_DATA[self.upgrade_level-1].get("upgrade_cost")*self.upgrade_discount)

        self.images[self.upgrade_level-1].convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def check_enemies(self, enemy_group):
        for enemy in enemy_group:
            self.target = enemy
            dist = ((enemy.rect.centerx - self.rect.centerx) ** 2 + (enemy.rect.centery - self.rect.centery) ** 2) ** 0.5
            if dist < self.range:
                self.target.health -= MAGMA_DATA[self.upgrade_level-1].get("damage")
                self.target.on_fire = True
            if dist > self.range:
                self.target.on_fire = False

    def range_updt(self, screen):
        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
        screen.blit(self.range_image, self.range_rect)