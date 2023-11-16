import pygame 
import sys 
from settings import Settings
from mainmenu import MainMenu
from tutorialmenu import TutorialMenu
from game import GameScreen
from monkey import Monkey
from leopard import Leopard


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    pygame.mixer.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Banánový žrút")
    
    # Create a clock object to control the FPS
    clock = pygame.time.Clock()
    fps = 60 

    # Create Monkey
    monkey = Monkey(settings, screen)

    # Screens 
    game_screen = GameScreen(screen, settings, monkey)
    main_menu = MainMenu(screen, settings)
    tutorial_menu = TutorialMenu(screen, settings)

    # Create Leopard
    leopard1 = Leopard(settings)
    leopard2 = Leopard(settings)
    leopard2.rect.x = settings.tile_size * 29
    leopard2.rect.y = settings.tile_size * 20

    # # Start the main loop for the game.
    current_screen = main_menu

    # Play the game music
    pygame.mixer.music.load("assets/sound/game_music2.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)  # Set the volume to half 


    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            flag = current_screen.handle_events(event)
            
            if flag != None:
                if flag == 1:
                    current_screen = game_screen
                if flag == 2:
                    current_screen = tutorial_menu
                elif flag == 3:
                    current_screen = main_menu
                elif flag == 4:
                    sys.exit()
                

        # Redraw the screen during each pass through the loop.
        if current_screen == game_screen:
            if game_screen.level == 1:
                n = current_screen.update(leopard1)
                game_screen.display(leopard1)
                if n != None:
                    current_screen = main_menu
                    game_screen.lives = 3

            else:
                n1 = current_screen.update(leopard1, leopard2)
                game_screen.display(leopard1, leopard2) 

                if n1 != None:
                    current_screen = main_menu
                    game_screen.lives = 3

        else:
            current_screen.display()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

        # Set FPS
        clock.tick(fps)
        
run_game()