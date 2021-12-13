import pygame
from vis import *
from model import *
from objects import *
from controller import *


# Game screen Height and Width
HEIGHT = 800
WIDTH = 1000


FPS = 30

'''flag = True
while flag:
    square = 0
    grid_lenght = int(input('Введите длину поля:'))
    grid_hieght = int(input('Введите ширину поля:'))
    MaxPalubn = int(input('Введите максимальную длину корабля:'))
    for i in range(MaxPalubn):
        square += (MaxPalubn - i + 2) * 3 * (i + 1)
    if grid_hieght * grid_lenght >= square / 2 + 10:
        flag = False'''


music = Music()
def main():
    """main function of the game, everything starts here"""
    pygame.init()
    Main = True
    Placement = False
    Game = False
    turn_of_player = True
    time_of_pressed = 0
    first_click = (10000, 10000)
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
        Main, Placement, Game, first_click, turn_of_player = event_manage(event, interface, Main, Placement, Game, first_click, turn_of_player, time_of_pressed)
        #print(time_of_pressed)
        pygame.display.update()
          
    pygame.quit()
    
    
main()