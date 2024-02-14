import pygame

class Player(pygame.sprite.Sprite):
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

    def movement(self, dt, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos.x += self.direction.x * speed * dt
        self.hitbox.x = round(self.pos.x)
        self.collision('horizontal')

        self.pos.y += self.direction.y * speed * dt
        self.hitbox.y = round(self.pos.y)
        self.collision('vertical')

        self.rect.center = self.hitbox.center


    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.pos.x = self.hitbox.x = sprite.hitbox.left - self.hitbox.size[0]
                    elif self.direction.x < 0:
                        self.pos.x = self.hitbox.x = sprite.hitbox.right

        elif direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.pos.y = self.hitbox.y = sprite.hitbox.top - self.hitbox.size[1]
                    elif self.direction.y < 0:
                        self.pos.y = self.hitbox.y = sprite.hitbox.bottom

    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
        self.image = self.image if self.facing_right else pygame.transform.flip(self.image, True, False)

    def update(self,dt):
        self.input()
        self.animate(dt)
        self.movement(dt, self.move_speed)
        