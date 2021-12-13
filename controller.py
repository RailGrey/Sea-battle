import model
from objects import *


def mouse_pos_check(mouse_pos, rect):
    """checks if mouse is on rect(left up angle, width, height)"""
    if abs(mouse_pos[0] - (rect[0] + rect[2] / 2)) <= rect[2] / 2 and abs(mouse_pos[1] - (rect[1] + rect[3] / 2)) <= \
            rect[3] / 2:
        return True
    else:
        return False


def event_manage(event, interface, main, placement, game, first_click, hit_posobility, time_of_pressed):
    """manages event from the game"""
    if event.type == pygame.MOUSEBUTTONDOWN:
        #if mouse on player grid
        if mouse_pos_check(event.pos, interface.grid_of_player.rect):  # if mouse on game window
            # if pressed button is left mouse button
            if event.button == 1 and placement:
                if first_click[0] == 10000:
                    first_click = event.pos
                else:
                    if first_click != mouse_grid_pose_check(event.pos, interface):
                        count = len(interface.grid_of_player.ships)
                        lenth = which_size(count, interface.grid_of_player.MaxPalubn)
                        first_click = (mouse_grid_pose_check(first_click, interface)[1], mouse_grid_pose_check(first_click, interface)[2])
                        second_click = (mouse_grid_pose_check(event.pos, interface)[1], mouse_grid_pose_check(event.pos, interface)[2])
                        model.manual_placement(interface.grid_of_player, first_click, second_click, lenth)  
                        first_click = (10000, 10000)
                        if len(interface.grid_of_player.ships) == (interface.grid_of_player.MaxPalubn + 1) * len(interface.grid_of_player.ships) // 2:
                            placement = False
        #if mouse on oponent grid
        #for Daniil!!!
        elif mouse_pos_check(event.pos, interface.grid_of_oponent.rect) and game:
            if event.button == 1:
                #last_attack_of_oponent = ''
                x = (mouse_grid_pose_check(event.pos, interface)[1], mouse_grid_pose_check(event.pos, interface)[2]) #coordinates in grid
                hit_posobility = model.player_hit(interface.grid_of_oponent, x) #step of player
                if not(model.is_alive(interface.grid_of_oponent.ships)): #end of game
                    interface.wining_screen('You win!')
                    model.placement_of_ship(interface.grid_of_oponent)
                    interface.grid_of_player.ships = []
                    interface.grid_of_player.miss = []
                    interface.grid_of_oponent.miss = []
                    interface.last_attack_of_oponent = ''
                    game = False
                if not(hit_posobility):
                    fire, interface.last_attack_of_oponent = model.oponent_turn(interface.grid_of_player)
                    while fire:
                        fire, interface.last_attack_of_oponent = model.oponent_turn(interface.grid_of_player)
                        if not(model.is_alive(interface.grid_of_player.ships)):
                            interface.wining_screen('Oponent win')
                            model.placement_of_ship(interface.grid_of_oponent)
                            interface.grid_of_player.ships = []
                            interface.grid_of_player.miss = []
                            interface.grid_of_oponent.miss = [] 
                            interface.last_attack_of_oponent = ''
                            game = False
        else:
            #if mouse on auto-placement button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.placement_of_ships.bg_rect) and not(game):
                interface.placement_of_ships.change_color()
                model.placement_of_ship(interface.grid_of_player)
            #if mouse on manual placement button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.manual_placement.bg_rect) and not(game):
                interface.manual_placement.change_color()                
                placement = True
                interface.grid_of_player.ships = []
            #if mouse on start button
            if mouse_pos_check(pygame.mouse.get_pos(), interface.start.bg_rect):
                interface.start.change_color() 
                if len(interface.grid_of_player.ships) == 0:
                    model.placement_of_ship(interface.grid_of_player)
                game = True

    return main, placement, game, first_click, hit_posobility


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
        block_size = grid.block_size
        left_x = grid.x
        right_x = grid.x + block_size * grid.lenght
        top_y = grid.y
        bot_y = grid.y + block_size * grid.height

        if left_x < mouse_pos[0] < right_x and top_y < mouse_pos[1] < bot_y:
            x = (mouse_pos[0] - left_x) // block_size + 1
            y = (mouse_pos[1] - top_y) // block_size + 1
            check_out = [grid, x, y]
    return check_out


def which_size(count, max_lenth):
    lenth = max_lenth
    size = 1
    flag = True
    while flag:
        if count < lenth:
            return size
        else:
            lenth += max_lenth - size
            size += 1
            if size == max_lenth + 1:
                return 0
