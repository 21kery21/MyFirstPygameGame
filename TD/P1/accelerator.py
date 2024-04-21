import pygame as pg
import constants as c
from accelerator_data import ACCELERATOR_DATA


class Accelerator(pg.sprite.Sprite):
    def __init__(self, images, tile_x, tile_y):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.x = (self.tile_x + 0.5) * c.TILE_SIZE
        self.y = (self.tile_y + 0.5) * c.TILE_SIZE
        self.selected = False
        self.range = ACCELERATOR_DATA[self.upgrade_level-1].get("range")
        self.org_range = ACCELERATOR_DATA[self.upgrade_level-1].get("range")
        self.acceleration = ACCELERATOR_DATA[self.upgrade_level-1].get("acceleration")
        self.upgrade_cost = ACCELERATOR_DATA[self.upgrade_level-1].get("upgrade_cost")
        self.upgrade_discount = 0
        self.target = None
        self.last_updt = pg.time.get_ticks()

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


    def update(self, sniper_group, turret_group, freeze_group, magma_group, screen):
        if pg.time.get_ticks() - self.last_updt > 500:
            self.last_updt = pg.time.get_ticks()
            self.range_updt(screen)
        self.load_images()
        self.cheak_weapons(sniper_group, turret_group, freeze_group, magma_group)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.selected:
            screen.blit(self.range_image, self.range_rect)

    def load_images(self):
        self.image = self.images[self.upgrade_level-1].convert_alpha()


    def upgrade(self):
        self.upgrade_level += 1
        self.range = ACCELERATOR_DATA[self.upgrade_level-1].get("range")
        self.org_range = ACCELERATOR_DATA[self.upgrade_level-1].get("range")
        self.acceleration = ACCELERATOR_DATA[self.upgrade_level-1].get("acceleration")
        self.upgrade_cost = ACCELERATOR_DATA[self.upgrade_level-1].get("upgrade_cost") - (ACCELERATOR_DATA[self.upgrade_level-1].get("upgrade_cost")*self.upgrade_discount)

        self.images[self.upgrade_level-1].convert_alpha()
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0,0,0))
        self.range_image.set_colorkey((0,0,0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def cheak_weapons(self, turret_group, sniper_group, freeze_group, magma_group):
        for sniper in sniper_group:
            self.target = sniper
            dist = ((sniper.rect.centerx - self.rect.centerx) ** 2 + (sniper.rect.centery - self.rect.centery) ** 2) ** 0.5
            if dist < self.range:
                self.target.cooldown = self.target.org_cooldown - self.acceleration
        for turret in turret_group:
            self.target = turret
            dist = ((turret.rect.centerx - self.rect.centerx) ** 2 + (turret.rect.centery - self.rect.centery) ** 2) ** 0.5
            if dist < self.range:
                self.target.cooldown = self.target.org_cooldown - self.acceleration
        for freeze in freeze_group:
            self.target = freeze
            dist = ((freeze.rect.centerx - self.rect.centerx) ** 2 + (freeze.rect.centery - self.rect.centery) ** 2) ** 0.5
            if dist < self.range:
                self.target.cooldown = self.target.org_cooldown - self.acceleration
        for magma in magma_group:
            self.target = magma
            dist = ((magma.rect.centerx - self.rect.centerx) ** 2 + (magma.rect.centery - self.rect.centery) ** 2) ** 0.5
            if dist < self.range:
                self.target.cooldown = self.target.org_cooldown - self.acceleration

            
    def range_updt(self, screen):
        self.range_image = pg.Surface((self.range * 2, self.range * 2))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center
        screen.blit(self.range_image, self.range_rect)

