import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)

block_size = 50


def draw_grid(x, y, lenght, hight, screen, scale):
    """Рисует сетку игрового поля.
    Input:
    x - х координата левого верхнего угла
    y - у координата левого верхнего угла
    lenght - длина сетки в клетках
    hight - высота сетки в клетках
    screen - объект типа pygame.screen, на нем производится отрисовка
    scale - масштаб клеток. Умножает 50 пикселей на это число. По стандарту следует ставить 1
    """
    # Горизонтальные линии
    for i in range(hight + 1):
        pygame.draw.line(screen, BLACK, (x, y + i * block_size * scale),
                         (x + lenght * block_size * scale, y + i * block_size * scale), 1)

    # Вертикальные линии
    for i in range(lenght + 1):
        pygame.draw.line(screen, BLACK, (x + i * block_size * scale, y),
                         (x + i * block_size * scale, y + hight * block_size * scale))
