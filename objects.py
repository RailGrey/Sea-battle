import pygame
import pygame.freetype

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN_BLUE = (0, 153, 153)
LIGHT_GRAY = (192, 192, 192)
RED = (255, 0, 0)
BLUE = (45, 48, 140)
ENEMY = (31, 191, 36)


class Possibility:
    """Класс для проверки возможности в расстановке
    Атрибуты:
        value - принимает False, True. Возможен ли этот вариант
        r_ship - координаты нового корабля
        dirrection - в каком направлении построить корабль. задается двумя значениями (z1, z2)
    """

    def __init__(self, value=True):
        self.value = value
        self.r_ship = []
        self.dirrection = (0, 0)


class Hit:
    """Класс для корректной работы хода игрока и опонента
    Атрибуты:
    possibilty - возможно ли выстрелить в эту точку поля.
    attack - была ли произведена атака. True - была, False - не была.
    exist - параметр для нахождения возможности добавить элемент в список промахов
    add_miss_possibilty - параметр для нахождения возможности добавить элемент в список промахов
    oponents_start_list - стартовая возможность ходов опонента. Представляет собой всё поле
    oponents_possible_hit - Реальная возможность выстрелов после тщательного обдумывания поля
    oponents_idea - True, если нужно выстрелить в определенные точки, False, если идей нет.
    idea - Куда нужно выстрелить по идее
    idea_ship - Корабль который по идее опонент собирается уничтожить
    create_idea_possibility - Возможность создания новой идеи. Если корабль был уничтожен,
                              то приходится снова надеятся на удачу.
    new_list - новый список клеток в которые можно стрелять
    choice_possibility - True, если можно выбрать клетку, False, если нельзя
    r_attack - Клетка которая была атакована
    new_idea - Новая идея, куда нужно стрелять.
    """

    def __init__(self):
        self.possibility = True
        self.attack = False
        self.exist = False
        self.add_miss_possibility = True
        self.oponents_start_list = []
        self.oponents_possible_hit = []
        self.oponents_idea = False
        self.idea = []
        self.idea_ship = None
        self.create_idea_possibility = True
        self.new_list = []
        self.choice_posibility = True
        self.r_attack = ()
        self.new_idea = []

class Ship:
    """
    Класс для кораблей
    --------------
    Атрибуты:
        grid - сетка к которой подвязан корабль #Можно будет заменить просто на Свой/Чужой. Или координату начала сетки
        r_live - массив вида [(x,y),...,(x,y)], для изначально живых клеток корабля. Нумерация начинается с 1,1
        r_dead - массив вида [(x,y),...,(x,y)], уничтоженых клеток корабля. Нумерация начинается с 1,1
        lenght - размер корабля в клетках.
        live - True, False. показывает жив ли корабль
        block_size - Размер блоков для отрисовки корабля.

    --------------
    Методы:
        draw_ship - Отрисовать просто корабль
        draw_dead_ship - Отрисовать убитый корабль (зачеркнутый)
        draw_enemy_dead_ship - Отрисовать вражеский корабль (уже убитый)
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
                                                      self.block_size, self.block_size))

    def draw_dead_ship(self):
        """
        Рисует крест на уничтоженой части корабля
        """
        for i in self.r_dead:
            pygame.draw.rect(self.grid.screen, BLUE, (self.grid.x + self.block_size * (i[0] - 1) + 1,
                                                      self.grid.y + self.block_size * (i[1] - 1) + 1,
                                                      self.block_size, self.block_size))
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
        block_size - длина клеток в пикселях
        color - цвет сетки
        ships - массив кораблей связаный с этой сеткой
        miss - массив с промахами
    ---------------
    Методы:
        draw_grid - Отрисовать сетку
        draw_your_ships - Отрисовать живые корабли
        draw_dead_your_ships - Отрисовать уничтоженые корабли
        draw_dead_enemy_ships - Отрисовать уничтоженые корабли врага
        draw_miss_shot - Отрисовать клетки по которым промахнулись, или стрелять в них нет смысла
    """

    def __init__(self, lenght, height, screen, MaxPalubn, black=(0, 0, 0), ships=None):
        if ships is None:
            ships = []
        self.x = 50
        self.y = 50
        self.lenght = lenght
        self.height = height
        self.screen = screen
        self.scale = 1
        self.block_size = 50 * self.scale
        self.color = black
        self.rect = 0
        self.ships = ships
        self.miss = []
        self.MaxPalubn=MaxPalubn

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

    def draw_your_ships(self):
        """Рисует корабли игрока на поле
        """
        for ship in self.ships:
            ship.draw_ship()

    def draw_dead_your_ships(self):
        """Рисует уничтоженые корабли игрока
        """
        for ship in self.ships:
            ship.draw_dead_ship()

    def draw_dead_enemy_ships(self):
        """Рисует уничтоженые корабли врага
        """
        for ship in self.ships:
            ship.draw_enemy_dead_ship()

    def draw_miss_shot(self):
        """Рисует промахи
        """
        for miss in self.miss:
            pygame.draw.circle(self.screen, self.color, (self.x + miss[0] * self.block_size - self.block_size // 2,
                                                         self.y + miss[1] * self.block_size - self.block_size // 2),
                               self.block_size // 8)


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
    
    
    def change_color(self):
        color = self.bg_color
        self.bg_color = self.text_color
        self.text_color = color


class Interface():
    """
    Содержит все элементы экрана
    ------
    grid_of_player - сетка игрока
    grid_of_oponent - сетка противника
    """

    def __init__(self, screen, width, height, grid_lenght, grid_height, MaxPalubn):
        self.screen = screen
        # create and place player's grid
        self.grid_of_player = Grid(grid_lenght, grid_height, screen, MaxPalubn, (0, 0, 0))
        block_size = min((width / 2 - 50) / self.grid_of_player.lenght,
                         (height - 250) / self.grid_of_player.height)
        self.grid_of_player.block_size = block_size
        self.grid_of_player.x = 25
        self.grid_of_player.y = 25
        self.grid_of_player.rect = (
            self.grid_of_player.x, self.grid_of_player.y, self.grid_of_player.lenght * self.grid_of_player.block_size,
            self.grid_of_player.height * self.grid_of_player.block_size)

        # create and place oponent's grid
        self.grid_of_oponent = Grid(grid_lenght, grid_height, screen, MaxPalubn, (0, 0, 0))
        self.grid_of_oponent.block_size = block_size
        self.grid_of_oponent.x = width / 2 + 25
        self.grid_of_oponent.y = 25
        self.grid_of_oponent.rect = (
            self.grid_of_oponent.x, self.grid_of_oponent.y,
            self.grid_of_oponent.lenght * self.grid_of_oponent.block_size,
            self.grid_of_oponent.height * self.grid_of_oponent.block_size)

        self.placement_of_ships = Button((50, 650, 100, 60), (0, 255, 0), (0, 0, 255), 50, 'Авто', 'Авто')
        self.manual_placement = Button((200, 650, 120, 60), (0, 255, 0), (0, 0, 255), 40, 'Ручная', 'Ручная')
        self.start = Button((450, 650, 150, 60), (0, 255, 0), (0, 0, 255), 30, 'Новая игра', 'Новая игра')
        self.grids = [self.grid_of_player, self.grid_of_oponent]
        self.last_attack_of_oponent = ''

    def draw(self, game):
        self.grid_of_player.draw_grid()
        self.grid_of_player.draw_miss_shot()
        self.grid_of_player.draw_your_ships()
        self.grid_of_player.draw_dead_your_ships()
        self.grid_of_oponent.draw_grid()
        self.grid_of_oponent.draw_dead_enemy_ships()
        self.start.draw(self.screen)
        if not (game):
            self.placement_of_ships.draw(self.screen)
            self.manual_placement.draw(self.screen)
        self.grid_of_oponent.draw_miss_shot()
        self.last_attack()
        
        
    def wining_screen(self, s):
        f = pygame.font.Font(None, 50)
        text = f.render(s, True, (0, 0, 0))
        self.screen.blit(text, (400, 500))            
        pygame.display.update()
        pygame.time.wait(2000) 
        
        
    def last_attack(self):
        f = pygame.font.Font(None, 50)
        text = f.render(str(self.last_attack_of_oponent), True, (0, 0, 0))
        self.screen.blit(text, (200, 500))            
        #pygame.display.update()
     
