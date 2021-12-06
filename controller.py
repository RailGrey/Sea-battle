def event_manage(event, field, pressed_mouse):
    """manages event from the game, changes field etc"""
    if event.type == pygame.MOUSEBUTTONDOWN:
        if mouse_pos_check(event.pos, interface.game_window):  # if mouse on game window
            # if pressed button is left mouse button
            if event.button == 1:
                pressed_mouse = True
            # checking if we need to zoom map
            zoom(event, field)
            # if mode is cell_spawn
            if interface.cell_spawn.pressed and event.button == 3:
                x_cell, y_cell = find_cell(event.pos, field, interface.game_window)
                settings.cell = field.cells[x_cell][y_cell]
                settings.update_cell()
                if x_cell != None:
                    field.cells[x_cell][y_cell].live = 5
        else:
            # if pressed button is left mouse button
            if event.button == 1:
                pressed_mouse = True
          
                


    return field, pressed_mouse, interface, speed