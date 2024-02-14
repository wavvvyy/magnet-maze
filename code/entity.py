import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

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