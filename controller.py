import model
import pygame

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
                
    #return field, pressed_mouse