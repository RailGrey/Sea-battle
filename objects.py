import pygame
import pygame.freetype

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
        """
        Рисует корабль игрока
        """
        for i in self.r_live:
            pygame.draw.rect(self.grid.screen, BLUE, (self.grid.x + self.block_size * (i[0] - 1) + 1,
                                                      self.grid.y + self.block_size * (i[1] - 1) + 1,
                                                      self.block_size - 1, self.block_size - 1))

    def draw_dead_ship(self):
        """
        Рисует крест на уничтоженой части корабля
        """
        for i in self.r_dead:
            pygame.draw.line(self.grid.screen, RED,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * (i[1] - 1)),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * i[1]), 5)

            pygame.draw.line(self.grid.screen, RED,
                             (self.grid.x + self.block_size * (i[0] - 1), self.grid.y + self.block_size * i[1]),
                             (self.grid.x + self.block_size * i[0], self.grid.y + self.block_size * (i[1] - 1)), 5)

    def draw_enemy_dead_ship(self):
        """
        Рисует сразу уничтоженый вражеский корабль
        """
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
        self.rect = 0

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
    Класс кнопок
       --------
       Атрибуты
       --------
       bg_rect = список [x, y, width, height] где x,y - координаты левого верхнего угла
       text_color - цвет текста
       bg_color - цвет фона
       size - размер шрифта
       text - текст
       text_pressed - текст при нажатии
    """
    def __init__(self, bg_rect: list, text_color, bg_color, size, text, text_pressed=''):
        """
        bg_rect = list [x, y, width, height] where x,y - coordinates of left top angle of rect of background
        text_color - color of bottom
        bg_color
        size
        text - text on the bottom
        text_pressed
        """
        self.text_color = text_color
        self.text = text
        self.bg_color = bg_color
        self.bg_rect = bg_rect
        self.text_rect = [0, 0, 0, 0]
        # pressed = 0 if not pressed and 1 if pressed
        self.pressed = 0
        self.pressed_color = (200, 200, 200)
        self.text_pressed = text_pressed
        self.size = size
        self.ships = 0

    def draw(self, screen):
        """draws button with text on the screen"""
        pygame.draw.rect(screen, self.bg_color, self.bg_rect)

        font = pygame.freetype.SysFont("Arial", self.size)  # FIXME text

        if (self.pressed == 0) or (self.text_pressed == '0'):
            font.render_to(screen, (self.bg_rect[0] + 5, self.bg_rect[1] + 5), self.text, fgcolor=self.text_color,
                           bgcolor=self.bg_color, size=self.size)
        else:
            font.render_to(screen, (self.bg_rect[0] + 5, self.bg_rect[1] + 5), self.text_pressed,
                           fgcolor=self.text_color, bgcolor=self.pressed_color, size=self.size)

        text_rect_fig = pygame.freetype.Font.get_rect(font, self.text, size=self.size)

        self.text_rect[0] = text_rect_fig.left
        self.text_rect[1] = text_rect_fig.top
        self.text_rect[2] = text_rect_fig.width
        self.text_rect[3] = text_rect_fig.height


class Interface():
    """
    Содержит все элементы экрана
    ------
    grid_of_player - сетка игрока
    grid_of_oponent - сетка противника
    """

    def __init__(self, screen, width, height):
        self.screen = screen
        # create and place player's grid
        self.grid_of_player = Grid(10, 10, screen, (0, 0, 0))
        block_size = min((width / 2 - 50) / self.grid_of_player.lenght,
                         (height - 250) / self.grid_of_player.height)
        self.grid_of_player.block_size = block_size
        self.grid_of_player.x = 25
        self.grid_of_player.y = 25
        self.grid_of_player.rect = (self.grid_of_player.x, self.grid_of_player.y, self.grid_of_player.lenght * self.grid_of_player.block_size,
                                    self.grid_of_player.height * self.grid_of_player.block_size)
        
        # create and place oponent's grid
        self.grid_of_oponent = Grid(10, 10, screen, (0, 0, 0))
        self.grid_of_oponent.block_size = block_size
        self.grid_of_oponent.x = width / 2 + 25
        self.grid_of_oponent.y = 25
        self.grid_of_oponent.rect = (self.grid_of_oponent.x, self.grid_of_oponent.y, self.grid_of_oponent.lenght * self.grid_of_oponent.block_size,
                                     self.grid_of_oponent.height * self.grid_of_oponent.block_size)        

        self.placement_of_ships = Button((50, 650, 100, 60), (0, 255, 0), (0, 0, 255), 50, 'Авто', 'Авто')
        

    def draw(self):
        self.grid_of_player.draw_grid()
        self.grid_of_oponent.draw_grid()
        self.placement_of_ships.draw(self.screen)
