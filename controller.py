import model
from objects import *
from vis import *


def mouse_pos_check(mouse_pos, rect):
    """checks if mouse is on rect(left up angle, width, height)"""
    if abs(mouse_pos[0] - (rect[0] + rect[2] / 2)) <= rect[2] / 2 and abs(mouse_pos[1] - (rect[1] + rect[3] / 2)) <= \
            rect[3] / 2:
        return True
    else:
        return False


manual_placement = Placement()


def event_manage(event, interface, placement, game, hit_posobility):
    """
    Manages event from the game
    ------
    Atributes
    ------
    event - событие
    interface - интерфейс программы, класса Interface
    placement - включен режим расстановки или нет
    game - началась ли игра или нет
    hit_posobility - может ли игрок атаковать
    """
    if manual_placement.process:
        draw_activate(interface.grid_of_player, manual_placement.first_click)
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.time.wait(70)
        # if mouse on player grid
        if mouse_pos_check(event.pos, interface.grid_of_player.rect):
            # if pressed button is left or right mouse button
            if (event.button == 1 or event.button == 3) and placement:
                if manual_placement.first_click != mouse_grid_pose_check(event.pos, interface) and event.button == 1:
                    # remake first click

                    manual_placement.first_click = ((mouse_grid_pose_check(event.pos, interface))[1],
                                                    (mouse_grid_pose_check(event.pos, interface))[2])
                    manual_placement.process = True
                    for ship in interface.grid_of_player.ships:
                        for i in ship.r_live:
                            if ((manual_placement.first_click[0] - i[0]) ** 2 + (
                                    manual_placement.first_click[1] - i[1]) ** 2) <= 2:
                                manual_placement.process = False
                elif event.button == 3 and manual_placement.process:  # tries to place a ship
                    count = len(interface.grid_of_player.ships)
                    lenth = model.which_size(count, interface.grid_of_player.MaxPalubn)
                    manual_placement.second_click = (
                        mouse_grid_pose_check(event.pos, interface)[1], mouse_grid_pose_check(event.pos, interface)[2])
                    model.manual_placement(interface.grid_of_player, manual_placement.first_click,
                                           manual_placement.second_click, lenth)
                    manual_placement.process = False
                    if len(interface.grid_of_player.ships) == (interface.grid_of_player.MaxPalubn + 1) * len(
                            interface.grid_of_player.ships) // 2:
                        placement = False
                    interface.draw_undo = True
        # if mouse on oponent grid and game started
        elif mouse_pos_check(event.pos, interface.grid_of_oponent.rect) and game:
            if event.button == 1:  # turn of player
                x = (mouse_grid_pose_check(event.pos, interface)[1],
<<<<<<< HEAD
                     mouse_grid_pose_check(event.pos, interface)[2]) #coordinates in grid
                hit_posobility = model.player_hit(interface.grid_of_oponent, x) #step of player
                if not(model.is_alive(interface.grid_of_oponent.ships)): # is it end of game?
                    interface.last_attack_of_oponent = ''
=======
                     mouse_grid_pose_check(event.pos, interface)[2])  # coordinates in grid
                hit_posobility = model.player_hit(interface.grid_of_oponent, x)  # step of player
                if not (model.is_alive(interface.grid_of_oponent.ships)):  # is it end of game?
>>>>>>> 32a5368244bbb33f2877a47a08b9a3893f88e024
                    interface.draw(game)
                    wining_screen('Победа!', interface.screen)
                    flag = True
                    while flag:
                        flag = model.try_to_place(interface.grid_of_oponent)
                    interface.grid_of_player.ships = []
                    interface.grid_of_player.miss = []
                    interface.grid_of_oponent.miss = []
                    game = False
                if not hit_posobility:  # turn of oponent
                    fire, interface.last_attack_of_oponent = model.oponent_turn(interface.grid_of_player)
                    while fire:  # fire - shows can bot attack or not
                        fire, interface.last_attack_of_oponent = model.oponent_turn(interface.grid_of_player)
                        if not (model.is_alive(interface.grid_of_player.ships)):
                            interface.last_attack_of_oponent = ''
                            interface.draw(game)
                            wining_screen('Порожение', interface.screen)
                            flag = True
                            while flag:
                                flag = model.try_to_place(interface.grid_of_oponent)
                            interface.grid_of_player.ships = []
                            interface.grid_of_player.miss = []
<<<<<<< HEAD
                            interface.grid_of_oponent.miss = [] 
=======
                            interface.grid_of_oponent.miss = []
                            interface.last_attack_of_oponent = ''
>>>>>>> 32a5368244bbb33f2877a47a08b9a3893f88e024
                            game = False
        else:
            # button section
            # if mouse on auto-placement button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.placement_of_ships.bg_rect) and not game:
                interface.placement_of_ships.change_color()
                flag = True
                while flag:
                    flag = model.try_to_place(interface.grid_of_player)
            # if mouse on manual placement button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.manual_placement.bg_rect) and not game:
                interface.manual_placement.change_color()
                placement = True
                interface.grid_of_player.ships = []
            # if mouse on start button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.start.bg_rect):
                interface.start.change_color()
                if game:
                    game = False
                    flag = True
                    while flag:
                        flag = model.try_to_place(interface.grid_of_oponent)
                    interface.grid_of_player.ships = []
                    interface.grid_of_player.miss = []
                    interface.grid_of_oponent.miss = []
                    interface.last_attack_of_oponent = ''
                else:
<<<<<<< HEAD
                    #game = True
                    if len(interface.grid_of_player.ships) < (interface.grid_of_player.MaxPalubn + 1) * interface.grid_of_player.MaxPalubn // 2:
=======
                    if len(interface.grid_of_player.ships) < (
                            interface.grid_of_player.MaxPalubn + 1) * interface.grid_of_player.MaxPalubn // 2:
>>>>>>> 32a5368244bbb33f2877a47a08b9a3893f88e024
                        flag = True
                        while flag:
                            flag = model.try_to_place(interface.grid_of_player)
                    #game = True
                    flag = True
                    while flag:
                        flag = model.try_to_place(interface.grid_of_oponent)
<<<<<<< HEAD
                    game = True
            #if mouse on undo button
=======
            # if mouse on undo button
>>>>>>> 32a5368244bbb33f2877a47a08b9a3893f88e024
            if mouse_pos_check(pygame.mouse.get_pos(), interface.undo.bg_rect) and interface.grid_of_player.ships != []:
                interface.grid_of_player.ships.pop()
                if len(interface.grid_of_player.ships) == 0:
                    interface.draw_undo = False

    return placement, game, hit_posobility


def mouse_grid_pose_check(mouse_pos, interface):
    """Проверяет положение мыши, в чьё поле попал клик, и координаты клика в клетках поля
    Input:
    mouse_pos - координаты мыши
    interface - объект класса Interface
    Output:
    check_out - массив [grid, x, y], где grid - сетка по которой кликнули, x,y - координаты клетки. None, в ином случае
    """
    check_out = None
    for grid in interface.grids:
        size_of_block = grid.block_size
        left_x = grid.x
        right_x = grid.x + size_of_block * grid.lenght
        top_y = grid.y
        bot_y = grid.y + size_of_block * grid.height

        if left_x < mouse_pos[0] < right_x and top_y < mouse_pos[1] < bot_y:
            x = (mouse_pos[0] - left_x) // size_of_block + 1
            y = (mouse_pos[1] - top_y) // size_of_block + 1
            check_out = [grid, x, y]
    return check_out
