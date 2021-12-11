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


grid_lenght = int(input('Введите длину поля: '))
grid_hieght = int(input('Введите ширину поля: '))
MaxPalubn = int(input('Введите максимальную длину корабля: '))

def main():
    """main function of the game, everything starts here"""
    pygame.init()
    Main = True
    Placement = False
    Game = False
    turn_of_player = True
    first_click = (10000, 10000)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    interface = Interface(screen, WIDTH, HEIGHT, grid_lenght, grid_hieght, MaxPalubn)
    placement_of_ship(interface.grid_of_oponent)
    while Main:
        screen.fill(WHITE)
        clock.tick(FPS)
        interface.draw(Game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Main = False
        Main, Placement, Game, first_click, turn_of_player = event_manage(event, interface, Main, Placement, Game, first_click, turn_of_player)
        pygame.display.update()
          
    pygame.quit()
    
    
main()