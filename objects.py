import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)
BLUE = (45, 48, 140)
ENEMY = (31, 191, 36)


class Ship:
    """
    Класс для кораблей
    --------------
    Атрибуты:
        grid - сетка к которой подвязан корабль #Можно будет заменить просто на Свой/Чужой. Или координату начала сетки
        r_live - массив вида [(x,y),...,(x,y)], для изначально живых клеток корабля. Нумерация начинается с 1,1
        r_dead - массив вида [(x,y),...,(x,y)], уничтоженых клеток корабля. Нумерация начинается с 1,1
        lenght - размер корабля в клетках.

    --------------
    Методы:


    """

    def __init__(self, grid, r_live, r_dead=None):
        if r_dead is None:
            r_dead = []
        self.grid = grid
        self.r_live = r_live  # [(1, 1)]
        self.r_dead = r_dead
        self.lenght = len(self.r_live)
        self.live = True
        self.block_size = grid.block_size

    def draw_ship(self):
        for i in self.r_live:
            pygame.draw.rect(self.grid.screen, BLUE, (self.grid.x + self.block_size * (i[0] - 1) + 1,
                                                      self.grid.y + self.block_size * (i[1] - 1) + 1,
                                                      self.block_size - 1, self.block_size - 1))

    def draw_dead_ship(self):
        for i in self.r_dead:
            pygame.draw.line(self.grid.screen, RED,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * (i[1] - 1)),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * i[1]), 5)

            pygame.draw.line(self.grid.screen, RED,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * i[1]),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * (i[1] - 1)), 5)

    def draw_enemy_dead_ship(self):
        for i in self.r_dead:
            pygame.draw.rect(self.grid.screen, ENEMY, (self.grid.x + self.block_size * (i[0] - 1) + 1,
                                                       self.grid.y + self.block_size * (i[1] - 1) + 1,
                                                       self.block_size - 1, self.block_size - 1))
            pygame.draw.line(self.grid.screen, BLACK,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * (i[1] - 1)),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * i[1]), 5)

            pygame.draw.line(self.grid.screen, BLACK,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * i[1]),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * (i[1] - 1)), 5)


class Grid:
    """
    Класс для сетки
    ---------------
    Атрибуты:
    x - x координата левого верхнего угла
    y - у координата левого верхнего угла
    lenght - длина сетки в клетках
    hight - высота сетки в клетках
    screen - экран на котором та сетка
    scale - масштаб. по стандарту 1 = 50 пикселей
    ---------------
    Методы:

    """

    def __init__(self, lenght, height, screen, black=(0, 0, 0)):
        self.x = 50
        self.y = 50
        self.lenght = lenght
        self.height = height
        self.screen = screen
        self.scale = 1
        self.block_size = 50 * self.scale
        self.color = black

    def draw_grid(self):
        """ Рисует сетку игрового поля.
        """
        # Горизонтальные линии
        for i in range(self.height + 1):
            pygame.draw.line(self.screen, self.color, (self.x, self.y + i * self.block_size),
                             (self.x + self.lenght * self.block_size, self.y + i * self.block_size), 1)

        # Вертикальные линии
        for i in range(self.lenght + 1):
            pygame.draw.line(self.screen, self.color, (self.x + i * self.block_size, self.y),
                             (self.x + i * self.block_size, self.y + self.height * self.block_size))


class Button:
    """
    Класс для кнопок
    ---------
    Атрибуты:
    х - х координата левого верхнего угла
    у - у координата левого верхнего угла
    width - ширина кнопки в пикселях
    height - высота кнопки в пикселях
    """

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Interface():
    """
    Содержит все элементы экрана
    ------
    """

    def __init__(self, screen, width, height):
        # create and place player's grid
        self.grid_of_player = Grid(10, 10, screen, (0, 0, 0))
        block_size = min((width / 2 - 50) / self.grid_of_player.lenght,
                         (height - 250) / self.grid_of_player.height)
        self.grid_of_player.block_size = block_size
        self.grid_of_player.x = 25
        self.grid_of_player.y = 25
        # create and place oponent's grid
        self.grid_of_oponent = Grid(10, 10, screen, (0, 0, 0))
        self.grid_of_oponent.block_size = block_size
        self.grid_of_oponent.x = width / 2 + 25
        self.grid_of_oponent.y = 25

        self.placement_of_ships = Button(500, 500, 30, 30)

    def draw(self):
        self.grid_of_player.draw_grid()
        self.grid_of_oponent.draw_grid()
