import model
from objects import *


def mouse_pos_check(mouse_pos, rect):
    """checks if mouse is on rect(left up angle, width, height)"""
    if abs(mouse_pos[0] - (rect[0] + rect[2] / 2)) <= rect[2] / 2 and abs(mouse_pos[1] - (rect[1] + rect[3] / 2)) <= \
            rect[3] / 2:
        return True
    else:
        return False


def event_manage(event, interface, pressed_mouse):
    """manages event from the game"""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mouse_pos_check(event.pos, interface.grid_of_player.rect):  # if mouse on game window
            # if pressed button is left mouse button
            if event.button == 1:
                pressed_mouse = True

        else:
            # if pressed button is left mouse button
            if event.button == 1:
                pressed_mouse = True
            if mouse_pos_check(pygame.mouse.get_pos(), interface.placement_of_ships.bg_rect):
                color = interface.placement_of_ships.bg_color
                interface.placement_of_ships.bg_color = interface.placement_of_ships.text_color
                interface.placement_of_ships.text_color = color
                model.placement_of_ship(interface.grid_of_player)
                print(interface.grid_of_player.ships)

    # return field, pressed_mouse


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
