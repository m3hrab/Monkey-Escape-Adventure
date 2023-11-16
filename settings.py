import pygame
class Settings():
    """A class to store all settings"""

    def __init__(self) -> None:
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (63, 72, 204)


        # menu settings 
        self.font = pygame.font.SysFont('assets/font/Roboto/Roboto-Regular.ttf', 24)
        self.title_font = pygame.font.SysFont('assets/font/Roboto/Roboto-Regular.ttf', 64) 
        self.button_width = 200
        self.button_height = 50
        self.button_color = (255, 255, 0)
        self.button_hover_color = (200, 200, 200)
        self.button_text_color = (0, 0, 0)
        self.button_text_hover_color = (0, 0, 0)


        # tutorial Settings 
        self.tutorial_text_font = pygame.font.SysFont('assets/font/Roboto/Roboto-Regular.ttf', 20)


        # Game settings
        self.monkey_speed = 2
        self.tile_size = 25


        # Monkey settings
        self.monkey_width = 25
        self.monkey_height = 25
    

        self.sound_on = True
        self.button_clicked_sound = pygame.mixer.Sound('assets/sound/btn.wav')
        self.banana_eaten_sound = pygame.mixer.Sound('assets/sound/eat.wav')
        self.level_up_sound = pygame.mixer.Sound('assets/sound/level_up.wav')
        self.lose_life = pygame.mixer.Sound('assets/sound/lose_life.wav')
