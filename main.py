import pygame
from vis import *
from model import *
from objects import *
from controller import *

BLACK = (0,0,0)
# Game screen Height and Width
HEIGHT = 800
WIDTH = 800

# window with game, rectangle(left up angle cors, width, height)
game_window = (0, 0, 800, 800)
FPS = 30


def main():
    """main function of the game, everything starts here"""
    global Main, screen
    pygame.init()
    Main = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    placement_of_ship()
    while Main:
        screen.fill(WHITE)
        clock.tick(FPS)
        draw_grid(10, 10, 10, 10, screen, 1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main = False        
        pygame.display.update()
    pygame.quit()
    
    
main()