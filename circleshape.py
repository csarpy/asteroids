import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.__position = pygame.Vector2(x, y)
        self.__velocity = pygame.Vector2(0, 0)
        self.__radius = radius

    def draw(self, screen):
        raise NotImplementedError ("Sub-classes must implement their own draw()")

    def update(self, dt):
        raise NotImplementedError ("Sub-classes must implement their own update()")

    def get_position(self):
        return self.__position
    
    def get_velocity(self):
        return self.__velocity
    
    def get_radius(self):
        return self.__radius
    
    # position is dynamic, so update it rather than set it
    def update_position(self, val):
        self.__position += val
    
    def set_velocity(self, val):
        self.__velocity = val
    
    def set_radius(self, val):
        self.__radius = val