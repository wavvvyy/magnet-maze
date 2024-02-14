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

        # self.add(groups)

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
        
        print(self.direction)

    def movement(self,dt, speed):
        self.pos.x += self.direction.x * speed * dt
        self.rect.x = round(self.pos.x)

        self.pos.y += self.direction.y * speed * dt
        self.rect.y = round(self.pos.y)

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def rotate(self, dt):
        self.rotation += 50 * dt
        self.image = pygame.transform.rotozoom(self.image, self.rotation, 1)

    def update(self,dt):
        print('in player update')
        self.input()
        # self.animate(dt)
        self.movement(dt, self.move_speed)
        # self.rotate(dt)