import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)

block_size = 50


def draw_activate(grid, r):
    """Показывает что мы активировали клетку
    Input:
    grid - сетка на которой это происходит
    r - координата клетки
    """
    pygame.draw.rect(grid.screen, GREEN_BLUE,
                     (grid.x + (r[0] - 1) * grid.block_size, grid.y + (r[1] - 1) * grid.block_size,
                      grid.block_size - 1, grid.block_size - 1), 5)


def first_screen(screen):
    f = pygame.font.Font(None, 50)
    text = f.render('Введите параметры в терминал', True, (255, 255, 255))
    screen.blit(text, (200, 400))
    pygame.display.update()

def wining_screen(s, screen):
    f = pygame.font.Font(None, 50)
    text = f.render(s, True, (0, 0, 0))
    screen.blit(text, (400, 500))
    pygame.display.update()
    pygame.time.wait(2000)
    
    
