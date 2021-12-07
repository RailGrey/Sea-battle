import pygame


class Ship:
    """
    Класс для кораблей
    --------------
    Атрибуты:
        grid - сетка к которой подвязан корабль #Можно будет заменить просто на Свой/Чужой. Или координату начала сетки
        r - массив с координатами клеток корабля (в клетках), относительно своей сетки.
        lenght - размер корабля в клетках.

    --------------
    Методы:

    """
    
    def __init__(self):
        self.grid = 0
        self.r = [(1, 1)]
        self.lenght = len(self.r)


    def __init__(self, grid, r_live, r_dead=None):
        if r_dead is None:
            r_dead = []
        self.grid = grid
        self.r_live = r_live  # [(1, 1)]
        self.r_dead = r_dead
        self.lenght = len(self.r_live)
        self.live = True


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

    """

    def __init__(self, x, y, lenght, height, screen, block_size=50, black=(0, 0, 0)):
        self.x = x
        self.y = y
        self.lenght = lenght
        self.height = height
        self.screen = screen
        self.scale = 1
        self.block_size = block_size * self.scale
        self.color = black
        
        
    def draw_grid(self):
        #Рисует сетку игрового поля.
        #    Input:
        #    grid - объект класса Grid
        
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
    '''
    Содержит все элементы экрана
    ------
    '''
    
    def __init__(self, screen):
        self.grid_of_player = Grid(50, 100, 10, 10, screen, 35, (0, 0, 0))
        self.grid_of_oponent = Grid(500, 100, 10, 10, screen, 35, (0, 0, 0))
        self.placement_of_ships = Button(500, 500, 30, 30)
        
        
        
    def draw(self):
        self.grid_of_player.draw_grid()
        self.grid_of_oponent.draw_grid()
        
    