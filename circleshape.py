import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, circle):
        return self.position.distance_to(circle.position) <= self.radius + circle.radius

    def draw(self, screen):
        raise NotImplementedError ("Sub-classes must implement their own draw()")

    def update(self, dt):
        raise NotImplementedError ("Sub-classes must implement their own update()")