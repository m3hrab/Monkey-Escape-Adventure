import pygame 
from button import Button
import sys

class MainMenu: 
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.buttons = [
            Button('Hrať', screen.get_width() // 2 - 100, screen.get_height() // 2 - 30,
                    self.settings.button_width, self.settings.button_height, 
                    self.settings.button_color, settings.button_hover_color,
                    self.play_game),
            Button('Návod', screen.get_width() // 2 - 100, screen.get_height() // 2 + 30,
                    self.settings.button_width, self.settings.button_height, 
                    self.settings.button_color, settings.button_hover_color,
                    self.show_instructions),
            Button('Ukončiť hru', screen.get_width() - 170, screen.get_height() - 100, 150, 40, 
                    (255, 0, 0), (200, 200, 200), self.quit_game)
        ]

        self.sound = pygame.image.load('assets/Images/sound.png')
        self.no_sound = pygame.image.load('assets/Images/no_sound.png')

        self.sound_rect = self.sound.get_rect()
        self.no_sound_rect = self.no_sound.get_rect()

        self.sound_rect.x = 50
        self.sound_rect.y = self.settings.screen_height - 100


    def play_game(self):
        pass

    def show_instructions(self):
        pass 

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self, event) -> int:
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.settings.sound_on:
                self.settings.button_clicked_sound.play()
                    
            if event.pos[0] > self.buttons[0].x and event.pos[0] < self.buttons[0].x + self.buttons[0].width:
                if event.pos[1] > self.buttons[0].y and event.pos[1] < self.buttons[0].y + self.buttons[0].height:
                    return 1
                elif event.pos[1] > self.buttons[1].y and event.pos[1] < self.buttons[1].y + self.buttons[1].height:
                    return 2

            elif event.pos[0] > self.buttons[2].x and event.pos[0] < self.buttons[2].x + self.buttons[2].width:
                if event.pos[1] > self.buttons[2].y and event.pos[1] < self.buttons[2].y + self.buttons[2].height:
                    return 4      

            elif event.pos[0] > self.sound_rect.x and event.pos[0] < self.sound_rect.x + self.sound_rect.width:
                if event.pos[1] > self.sound_rect.y and event.pos[1] < self.sound_rect.y + self.sound_rect.height:
                    self.settings.sound_on = not self.settings.sound_on
                    if self.settings.sound_on:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()


    def display(self):
        self.screen.fill(self.settings.bg_color)
        title_surface = self.settings.title_font.render('Banánový žrút', True, self.settings.button_color)
        self.screen.blit(title_surface, (self.screen.get_width() // 2 - title_surface.get_width() // 2, 150))

        for button in self.buttons:
            button.draw(self.screen, self.settings.font)

        if self.settings.sound_on:
            self.screen.blit(self.sound, self.sound_rect)
        else:
            self.screen.blit(self.no_sound, self.sound_rect)



