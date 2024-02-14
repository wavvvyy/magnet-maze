import pygame
from settings import *
from player import Player
from visible_sprites_group import VisibleSpritesGroup

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = VisibleSpritesGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x =  col_index * TILE_SIZE
                y =  row_index * TILE_SIZE 

                if col == 'x':
                    pass
                elif col == 'p':
                    self.player = Player((x,y),[self.visible_sprites])
                    

    def update(self, dt):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update(dt)