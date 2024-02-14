import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.frames = [pygame.image.load(f'./graphics/frames/{i}.png').convert_alpha() for i in range(1,7)]
        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midleft = pos)
        self.hitbox = self.rect.inflate(0,-25)

        self.direction = pygame.math.Vector2()
        self.move_speed = 200
        self.animation_speed = 5

        self.pos = pygame.math.Vector2(self.hitbox.topleft)
        self.obstacle_sprites = obstacle_sprites

        self.facing_right = True

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_right = False
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_right = True
        else:
            self.direction.x = 0

    def update(self,dt):
        self.input()
        self.animate(dt)
        self.movement(dt, self.move_speed)
        