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
