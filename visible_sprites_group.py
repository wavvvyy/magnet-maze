import pygame

class VisibleSpritesGroup(pygame.sprite.Group):
    def update(self, dt):

        print(self.sprites())

        for sprite in self.sprites():
            sprite.update(dt)