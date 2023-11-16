import pygame 
import math


class Monkey():
    """A class to handle the monkey"""
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen 
        
        # Load the monkey image and get its rect
        self.images = self.load_images()
        self.image = self.images['right'][0]
        self.image = pygame.transform.scale(self.image, (self.settings.monkey_width, self.settings.monkey_height))
        self.rect = self.image.get_rect()

        #  Monkey's starting position
        self.rect.x = self.settings.tile_size * 18
        self.rect.y = self.settings.tile_size * 7

        # Monkey's movement flags
        self.moving = {'right': False, 'left': False, 'up': False, 'down': False} 
        self.pos = {'x':float(self.rect.x), 'y':float(self.rect.y)}
        self.direction = None

        # Monkey's animation
        self.animation = {'delay': 60, 'frame': 0, 'last_update': pygame.time.get_ticks(), 'direction': None}
        self.animation_counter = 0

    def load_images(self):
        images = {}
        images['left'] = [pygame.image.load(f'assets/Images/monkey/R{i}.png') for i in range(1, 5)]
        images['right'] = [pygame.image.load(f'assets/Images/monkey/L{i}.png') for i in range(1, 5)]
        images['up'] = [pygame.image.load('assets/Images/monkey/UP.png')]
        images['down'] = [pygame.image.load('assets/Images/monkey/DOWN.png')]
        
        return images


    def update(self, map_data):
        """Update the monkey's position based on the movement flags."""
        for direction, moving in self.moving.items():
            if moving:
                new_pos = self.rect.copy() 
                # Update the monkey's position
                if direction == 'left':
                    new_pos[0] -= self.settings.monkey_speed 
                    self.direction = 'left'
                elif direction == 'right':
                    new_pos[0] += self.settings.monkey_speed
                    self.direction = 'right'
                elif direction == 'up':
                    new_pos[1] -= self.settings.monkey_speed 
                    self.direction = 'up'
                elif direction == 'down':
                    new_pos[1] += self.settings.monkey_speed 
                    self.direction = 'down'


                if direction == 'down' or direction == 'right':
                    n = math.ceil(round(new_pos[0]) / self.settings.tile_size)
                    m = math.ceil(round(new_pos[1]) / self.settings.tile_size)
                elif direction == 'up' or direction == 'left':
                    n = math.floor(round(new_pos[0]) / self.settings.tile_size)
                    m = math.floor(round(new_pos[1]) / self.settings.tile_size)

                # Check if the monkey is on the tile
                if map_data[m][n] == 1:
                    self.moving[direction] = False
                # Update the monkey's position
                self.rect.x = round(new_pos[0])
                self.rect.y = round(new_pos[1]) 




    def display(self):
        """Draw the animated monkey at its current location."""
        if self.direction in self.images:
            # Update the animation frame
            self.animation_counter += 1
            if self.animation_counter >= len(self.images[self.direction]):
                self.animation_counter = 0

            self.image = self.images[self.direction][self.animation_counter]

        self.image = pygame.transform.scale(self.image, (25,25))
        self.screen.blit(self.image, self.rect)