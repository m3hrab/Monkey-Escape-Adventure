import pygame
import sys

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, function=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.function = function 
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, font):
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] < self.x + self.width and self.y < mouse[1] < self.y + self.height:
            pygame.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height))
            if pygame.mouse.get_pressed()[0] and self.function is not None:
                self.function()
        else:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

        text_surface = font.render(self.text, True, (0, 0, 0))
        screen.blit(text_surface, (self.x + (self.width - text_surface.get_width()) // 2, self.y + (self.height - text_surface.get_height()) // 2))
