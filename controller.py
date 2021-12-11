import model
from objects import *


def mouse_pos_check(mouse_pos, rect):
    """checks if mouse is on rect(left up angle, width, height)"""
    if abs(mouse_pos[0] - (rect[0] + rect[2] / 2)) <= rect[2] / 2 and abs(mouse_pos[1] - (rect[1] + rect[3] / 2)) <= \
            rect[3] / 2:
        return True
    else:
        return False


def event_manage(event, interface, placement, game, first_click):
    """manages event from the game"""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mouse_pos_check(event.pos, interface.grid_of_player.rect):  # if mouse on game window
            # if pressed button is left mouse button
            if event.button == 1 and placement:
                if first_click[0] == 10000:
                    first_click = event.pos
                else:
                    count = len(interface.grid_of_player.ships)
                    print(count)
                    if count < 4:
                        lenth = 1
                    elif count < 7:
                        lenth = 2
                    elif count < 9:
                        lenth = 3
                    else:
                        lenth = 4
                    first_click = (mouse_grid_pose_check(first_click, interface)[1], mouse_grid_pose_check(first_click, interface)[2])
                    second_click = (mouse_grid_pose_check(event.pos, interface)[1], mouse_grid_pose_check(event.pos, interface)[2])
                    model.manual_placement(interface.grid_of_player, first_click, second_click, lenth)  
                    first_click = (10000, 10000)

        else:
            # if pressed button is left mouse button
            if event.button == 1:
                pressed_mouse = True
            if mouse_pos_check(pygame.mouse.get_pos(), interface.placement_of_ships.bg_rect) and not(game):
                color = interface.placement_of_ships.bg_color
                interface.placement_of_ships.bg_color = interface.placement_of_ships.text_color
                interface.placement_of_ships.text_color = color
                model.placement_of_ship(interface.grid_of_player)
            if mouse_pos_check(pygame.mouse.get_pos(), interface.manual_placement.bg_rect) and not(game):
                color = interface.manual_placement.bg_color
                interface.manual_placement.bg_color = interface.manual_placement.text_color
                interface.manual_placement.text_color = color                
                placement = True
                interface.grid_of_player.ships = []
    
    return placement, game, first_click


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
