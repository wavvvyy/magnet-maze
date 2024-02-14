import pygame
from settings import *
from player import Player
from visible_sprites_group import VisibleSpritesGroup
from tile import Tile

class Level:
    def __init__(self):

        self.screen = pygame.display.get_surface()

        self.visible_sprites = VisibleSpritesGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x =  col_index * TILE_SIZE
                y =  row_index * TILE_SIZE 

                if col == 'x':
                    self.tile = Tile((x,y),[self.visible_sprites, self.obstacle_sprites])

                elif col == 'p':
                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
                    

    def update(self, dt):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update(dt)