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
    # main cycle of the game, ends when player exits the game,
    # consists of 2-3 cycles: game menu, game play, game over/game pause !!!Still in discussion about it!!!
    while Main:
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        Main = False

    pygame.quit()
    
    
main()