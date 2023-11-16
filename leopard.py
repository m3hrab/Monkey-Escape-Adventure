import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class Leopard():

    def __init__(self, settings) -> None:

        self.settings = settings
        self.images = {
            'left': [pygame.image.load(f'assets/Images/leopard/left{i}.png') for i in range(1, 3)],
            'right': [pygame.image.load(f'assets/Images/leopard/right{i}.png') for i in range(1, 3)],
            'up': [pygame.image.load(f'assets/Images/leopard/up{i}.png') for i in range(1, 3)],
            'down': [pygame.image.load(f'assets/Images/leopard/down{i}.png') for i in range(1, 3)],
        }

        
        self.image = pygame.transform.scale(self.images['right'][0], (self.settings.tile_size, self.settings.tile_size))
        self.animation_counter = 0

        self.rect = self.image.get_rect()
        self.rect.x = self.settings.tile_size * 2
        self.rect.y = self.settings.tile_size * 3

        self.speed = 20
        self.move_counter = 0



    def update(self, monkey_position, map_data):
        
        matrix = [[1 if cell == 0 else 0 for cell in row] for row in map_data]
        grid = Grid(matrix=matrix)
        position = (self.rect.x // self.settings.tile_size, self.rect.y // self.settings.tile_size)
        target = (monkey_position[0], monkey_position[1])

        start = grid.node(position[0], position[1])
        end = grid.node(target[0], target[1])

        finder = AStarFinder()
        path, runs = finder.find_path(start, end, grid)
        
        if len(path) > 1:
            self.move_counter += 1
            if self.move_counter >= self.speed:
                self.move_counter = 0
                self.rect.x = path[1].x * self.settings.tile_size
                self.rect.y = path[1].y * self.settings.tile_size 

                next_position = (path[1].x, path[1].y)

                if next_position[0] > position[0]:
                    self.image = self.images['right'][self.animation_counter % 2]
                elif next_position[0] < position[0]:  
                    self.image = self.images['left'][self.animation_counter % 2]
                elif next_position[1] > position[1]:
                    self.image = self.images['down'][self.animation_counter % 2]
                elif next_position[1] < position[1]:
                    self.image = self.images['up'][self.animation_counter % 2]

            self.animation_counter += 1 


    def draw(self, screen):
        self.image = pygame.transform.scale(self.image, (25, 25))
        screen.blit(self.image, self.rect)  
        