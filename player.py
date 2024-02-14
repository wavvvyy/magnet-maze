import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        
        # self.frames = [pygame.image.load(f'frames/{i}.png').convert_alpha() for i in range(1,7)]
        # self.frame_index = 0

        # self.image = self.frames[self.frame_index]
        self.image = pygame.image.load('frames/1.png')
        self.rect = self.image.get_rect(midleft = pos)

        self.direction = pygame.math.Vector2()
        self.move_speed = 200
        self.animation_speed = 5

        self.pos = pygame.math.Vector2(self.rect.topleft)
        print('helo')

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
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def movement(self,dt, speed):
        self.pos.x += self.direction.x * speed * dt
        self.rect.x = round(self.pos.x)

        self.pos.y += self.direction.y * speed * dt
        self.rect.y = round(self.pos.y)

    def update(self,dt):
        self.input()
        self.movement(dt, self.move_speed)