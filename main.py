import pygame
from vis import *
from model import *
from objects import *
from controller import *


# Game screen Height and Width
HEIGHT = 800
WIDTH = 1000

FPS = 30

music = Music()
def main():
    """main function of the game, everything starts here"""
    pygame.init()
    Main = True
    Placement = False
    Game = False
    turn_of_player = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    first_screen(screen)
    grid_lenght, grid_hieght, MaxPalubn = initial(screen)    
    interface = Interface(screen, WIDTH, HEIGHT, grid_lenght, grid_hieght, MaxPalubn)
    music.check_situation(interface)
    music.play_music()
    while Main:
        screen.fill(WHITE)
        clock.tick(FPS)
        interface.draw(Game)
        music.check_situation(interface)
        music.check_and_play()
        music.check_end_game(Game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main = False
        Placement, Game, turn_of_player = event_manage(event, interface, Placement, Game, turn_of_player)
        pygame.display.update()
          
    pygame.quit()
    
    
main()