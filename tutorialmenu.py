import pygame , sys
from button import Button

class TutorialMenu():
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings

        self.tutorial_text = """   
        Ovládanie:
        Použite šípky (Hore, Dole, Vľavo, Vpravo), aby ste usmernili svoju opicu cez 
        bludisko.Tlačidlo "Pauza" uprostred obrazovky vám umožní zastaviť a pokračovať
        v hre. Ak vás lev chytí, stratíte život a obnovíte sa v strede bludiska.

        Skóre:
        Za každú zbieranú banánovú bodku získate 10 bodov. Vaše skóre je zobrazené v 
        pravom hornom rohu obrazovky.Pre postup na ďalšiu úroveň musíte zozbierať všetky
        banány na aktuálnej úrovni.
        
        Postup v hre:
        Začnite s ľahkou úrovňou, kde je menej levov pre hladší začiatok.
        Vašou úlohou je zozbierať všetky banány na aktuálnej úrovni.
        Po úspešnom skončení sa na obrazovke zobrazí vaše skóre a budete mať
        možnosť pokračovať na ďalšiu úroveň alebo sa vrátiť na hlavnú obrazovku.
        Dôležité je sledovať svoje tri životy v ľavom dolnom rohu obrazovky. Ak vám 
        dojdú životy, vrátite sa na hlavnú obrazovku.
        """

        self.tutorial_lines = self.tutorial_text.split('\n')
        self.tutorial_text_surface = self.settings.tutorial_text_font.render(self.tutorial_text,
                                                                            True, (255, 255, 255))
        self.tutorial_text_rect = self.tutorial_text_surface.get_rect()
        self.tutorial_text_rect.center = (400, 300) 

        self.buttons = [
            Button('Späť', 50, screen.get_height() - 70, 100, 40, (255, 255, 0), (200, 200, 200)),
            Button('Ukončiť hru', screen.get_width() - 170, 
                    screen.get_height() - 70, 150, 40, (255, 0, 0), (200, 200, 200), self.quit_game)
        ]

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.settings.sound_on:
                self.settings.button_clicked_sound.play()
                
            if event.pos[0] > self.buttons[0].x and event.pos[0] < self.buttons[0].x + self.buttons[0].width:
                if event.pos[1] > self.buttons[0].y and event.pos[1] < self.buttons[0].y + self.buttons[0].height:
                    return 3
                elif event.pos[1] > self.buttons[1].y and event.pos[1] < self.buttons[1].y + self.buttons[1].height:
                    return 4

    def display(self):

        self.screen.fill(self.settings.bg_color)
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(50, 50, 700, 460))
        y = 50  # Starting y position of the text
        for line in self.tutorial_lines:
            line_surface = self.settings.tutorial_text_font.render(line, True, (255, 255, 255))
            line_rect = line_surface.get_rect()
            line_rect.center = (400, y)
            self.screen.blit(line_surface, line_rect)
            y += line_surface.get_height() + 10 

        for button in self.buttons:
            button.draw(self.screen, self.settings.font)