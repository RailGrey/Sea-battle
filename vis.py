import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)

block_size = 50


class Grid:
    """Класс для рисовки сетки. x,y - верхний левый угол
     lenght, hight - размеры сетки. scale - масштаб
     """

    def __init__(self, screen, scale=1):
        self.x = 0
        self.y = 0
        self.lenght = 0
        self.hight = 0
        self.screen = screen
        self.scale = scale
        self.block_size = block_size * self.scale

    def draw_grid(self):
        # Горизонтальные линии
        for i in range(self.hight + 1):
            pygame.draw.line(self.screen, BLACK, (self.x, self.y + i * self.block_size),
                             (self.x + self.lenght * self.block_size, self.y + i * self.block_size), 1)

        # Вертикальные линии
        for i in range(self.lenght + 1):
            pygame.draw.line(self.screen, BLACK, (self.x + i * self.block_size, self.y),
                             (self.x + i * self.block_size, self.y + self.hight * self.block_size))
