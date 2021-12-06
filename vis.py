import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)

block_size = 50

def draw_grid(x, y, lenght, hight, screen, scale):
    # Горизонтальные линии
    for i in range(hight + 1):
        pygame.draw.line(screen, BLACK, (x, y + i * block_size * scale),
                         (x + lenght * block_size * scale, y + i * block_size * scale), 1)

    # Вертикальные линии
    for i in range(lenght + 1):
        pygame.draw.line(screen, BLACK, (x + i * block_size * scale, y),
                         (x + i * block_size * scale, y + hight * block_size * scale))
