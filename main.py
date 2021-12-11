import pygame
from vis import *
from model import *
from objects import *
from controller import *

BLACK = (0,0,0)
# Game screen Height and Width
HEIGHT = 800
WIDTH = 1000

# window with game, rectangle(left up angle cors, width, height)
game_window = (0, 0, 800, 800)
FPS = 10


def main():
    """main function of the game, everything starts here"""
    global Main, screen
    pygame.init()
    Main = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    interface = Interface(screen, WIDTH, HEIGHT)
    placement_of_ship(interface.grid_of_oponent)
    while Main:
        screen.fill(WHITE)
        clock.tick(FPS)
        interface.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main = False
        event_manage(event, interface, 1)
        pygame.display.update()
    pygame.quit()
    
    
main()