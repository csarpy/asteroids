from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.__rotation = 0

    def triangle(self):
        position = self.get_position()
        radius = self.get_radius()
        rotation = self.get_rotation()
        forward = pygame.Vector2(0, 1).rotate(rotation)
        right = pygame.Vector2(0, 1).rotate(rotation + 90) * radius / 1.5
        a = position + forward * radius
        b = position - forward * radius - right
        c = position - forward * radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.update_rotation((PLAYER_TURN_SPEED * dt))

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.get_rotation())
        self.update_position(forward * PLAYER_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # turn left
            self.rotate(dt * -1)

        if keys[pygame.K_d]:
            # turn right
            self.rotate(dt)

        if keys[pygame.K_w]:
            # go forward
            self.move(dt)

        if keys[pygame.K_s]:
            # go back
            self.move(dt * -1)

    # rotation is dynamic, so update it rather than set it
    def update_rotation(self, value):
        self.__rotation += value
    
    def get_rotation(self):
        return self.__rotation