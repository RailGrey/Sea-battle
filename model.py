import pygame
import random
from controller import mouse_pos_check
from objects import *


def is_alive(ships):
    for i in range(len(ships)):
        if ships[i].live:
            return True
    return False


def modul(mod):
    if mod >= 0:
        return mod
    else:
        return -mod


def sign(sig):  # int
    if sig == 0:
        return 0
    else:
        return int(sig / modul(sig))


def placement_of_ship(grid):
    MaxPalubn = grid.MaxPalubn
    intXboard = grid.lenght
    intYboard = grid.height
    ###!!! тут номерация с 0, но переводится в итоге с 1 как и требуется в других частях кода
    ShipsPositions = []
    Positions_list = [(i * 10 ** len(str(max(intXboard, intYboard) - 1)) + j) for i in range(intXboard) for j in
                      range(intYboard)]
    # for m in range(MaxPalubn-1,-1,-1):
    m = MaxPalubn - 1
    while m > -1:
        n = 0
        # Spawn (m+1)-x
        while n <= MaxPalubn - 1 - m:
            position = random.randint(0, len(Positions_list) - 1)

            x = Positions_list[position] // (10 ** len(str(max(intXboard, intYboard) - 1)))
            y = Positions_list[position] - 10 ** len(str(max(intXboard, intYboard) - 1)) * x

            popit = 0
            zacicl = 0
            while popit == 0 and zacicl < 4:
                rot1 = random.randint(1, 4)  # Change rotation 1-up,2-right,3-down,4-left
                rot2 = random.randint(0, 1)
                rotY = int((1 - (-1) ** rot1) * (0.5 - rot2))
                rotX = int((1 - (-1) ** (rot1 - 1)) * (0.5 - rot2))
                popit = 1
                zacicl += 1
                print("popit crash")
                if 0 <= (x + m * rotX) <= intXboard - 1 and 0 <= (y + m * rotY) <= intYboard - 1:

                    try:
                        Positions_list.index(
                            (x + m * rotX) * (10 ** len(str(max(intXboard, intYboard) - 1))) + (y + m * rotY))
                    except ValueError:
                        popit = 0
                        # print("исключения есть")
                    else:
                        popit = 1
                        # print("исключений нет")

                else:
                    popit = 0
                    # print("исключения есть")

            Yaround = -1 - m * (1 - sign(rotY + 0.5)) // 2
            Xaround = -1 - m * (1 - sign(rotX + 0.5)) // 2

            Del_list = [-1 for i in range(3 * (3 + m))]
            i = 0
            while Xaround <= 1 + (1 + (m - 1) * modul(rotX)) * (
                    1 + sign(rotX)) // 2:  # Что удаляем из возможных позиций
                while Yaround <= 1 + (1 + (m - 1) * modul(rotY)) * (1 + sign(rotY)) // 2 and i <= 3 * (3 + m) - 1:
                    # print(x+Xaround,y+Yaround)
                    if 0 <= x + Xaround <= intXboard - 1 and 0 <= y + Yaround <= intYboard - 1:
                        Del_list[i] = (x + Xaround) * (10 ** len(str(max(intXboard, intYboard) - 1))) + y + Yaround
                        Yaround += 1
                        i += 1
                    else:
                        Del_list[i] = -1
                        Yaround += 1
                        i += 1
                Xaround += 1
                Yaround = -1 - m * (1 - sign(rotY + 0.5)) // 2

            Yaround = -m * (1 - sign(rotY + 0.5)) // 2
            Xaround = -m * (1 - sign(rotX + 0.5)) // 2
            i = 0
            S = []
            while Xaround <= (1 + (m - 1) * modul(rotX)) * (
                    1 + sign(rotX)) // 2:  # Что добавляем в позиции вражеских кораблей
                while Yaround <= (1 + (m - 1) * modul(rotY)) * (1 + sign(rotY)) // 2:
                    S += [(x + Xaround + 1, y + Yaround + 1)]
                    Yaround += 1
                Xaround += 1
                Yaround = -m * (1 - sign(rotY + 0.5)) // 2

            ShipsPositions.append(Ship(grid, S))
            i = 0
            while i <= (len(Del_list) - 1):
                if Del_list[i] != -1:
                    try:
                        Positions_list.remove(int(Del_list[i]))
                        i += 1
                    except ValueError:
                        i += 1
                else:
                    i += 1
            n += 1
            if zacicl == 4:
                m = MaxPalubn
                n = 0
                ShipsPositions = []
                Positions_list = [(i * 10 ** len(str(max(intXboard, intYboard) - 1)) + j) for i in range(intXboard) for
                                  j in range(intYboard)]
        m -= 1
        # end of Spawn (m+1)-x
    # popitshipplacement=1
    grid.ships = ShipsPositions


def manual_placement(grid, r1, r2, len_ship):
    """Функция для ручной расстановки кораблей
     Input:
     grid - сетка класса Grid
     r1 - координата (х, у)
     r2 - вторая координата (x,y)
     len_ship - длина корабля
     """
    possibility = Possibility()
    delta_rx = r2[0] - r1[0]
    delta_ry = r2[1] - r1[1]
    if len_ship != 1:
        if r1 == r2:
            possibility.value = False

    for ship in grid.ships:
        for i in ship.r_live:
            if ((r1[0] - i[0]) ** 2 + (r1[1] - i[1]) ** 2) <= 2:
                possibility.value = False

    if possibility.value:
        if delta_ry > delta_rx and delta_ry > -delta_rx:
            possibility.dirrection = (0, 1)
            if r1[1] - len_ship < 0:
                possibility.value = False
        elif delta_rx < delta_ry < -delta_rx:
            possibility.dirrection = (-1, 0)
            if r1[0] - len_ship < 0:
                possibility.value = False
        elif delta_rx > delta_ry > -delta_rx:
            possibility.dirrection = (1, 0)
            if r1[0] + len_ship > grid.lenght + 1:
                possibility.value = False
        elif delta_ry < delta_rx and delta_ry < -delta_rx:
            possibility.dirrection = (0, -1)
            if r1[1] + len_ship > grid.height + 1:
                possibility.value = False

        if r1[0] + possibility.dirrection[0] * len_ship < 0 or r1[0] + possibility.dirrection[0] * len_ship > grid.lenght:
            possibility.value = False
        if r1[1] + possibility.dirrection[1] * len_ship < 0 or r1[1] + possibility.dirrection[1] * len_ship > grid.height:
            possibility.value = False

        if possibility.value:
            for i in range(len_ship):
                possibility.r_ship += [(r1[0] + possibility.dirrection[0] * i, r1[1] + possibility.dirrection[1] * i)]
            for r in possibility.r_ship:
                for ship in grid.ships:
                    for i in ship.r_live:
                        if ((r[0] - i[0]) ** 2 + (r[1] - i[1]) ** 2) <= 2:
                            possibility.value = False

    if possibility.value:
        new_ship = Ship(grid, possibility.r_ship)
        grid.ships += [new_ship]

    elif not possibility.value:
        print('Нельзя поставить так')


def player_hit(grid, r):
    """Совершает ход игрока. Уничтожает корабль врага если попал, и промахивается иначе.
    Возвращает True, если нужен еще 1 ход.
    Input:
        grid - объект класса Grid. Вражеская сетка
        r - координаты в клетках (x, y)
    Return:
        True - Если нужно дать еще один ход
        False - Если не нужно
    """
    hit = Hit()
    for i in grid.miss:
        if r == i:
            hit.possibility = False
    for i in grid.ships:
        for j in i.r_dead:
            if r == j:
                hit.possibility = False
    if hit.possibility:
        for ship in grid.ships:
            for i in ship.r_live:
                if r == i:
                    ship.r_dead.append((int(r[0]), int(r[1])))
                    ship.r_live.remove(i)
                    hit.attack = True
                    add_miss_after_hit(grid, hit, r)
                    if not ship.r_live:
                        ship.live = False
                        add_miss_after_death(grid, ship, hit)

        if not hit.attack:
            grid.miss.append(r)
    output = not hit.possibility or hit.attack
    return output


oponent_hit = Hit()


def oponent_turn(grid):
    """Ход опонента. По сетке определяет куда можно выстрелить. Если опонент попал возвращает True
    Использует вспомогательный класс Hit и объект oponent_hit.
    Input:
    grid - сетка класса Grid, которую нужно проанализировать и сделать ход
    Return:
    True - если попал и нужен еще 1 ход
    False - если ход опонента закончен
    oponent_hit.r_attack - координата выстрела опонента"""
    oponent_hit.attack = False
    oponent_hit.oponents_start_list = [(i, j) for i in (range(1, grid.lenght + 1, 1)) for j in
                                       (range(1, grid.height + 1, 1))]

    create_new_list_of_possible_blocks(grid, oponent_hit)
    create_new_idea(grid, oponent_hit)

    if oponent_hit.oponents_idea:
        r_attack_index = random.randint(0, len(oponent_hit.idea) - 1)
        oponent_hit.r_attack = oponent_hit.idea[r_attack_index]
        oponent_attack(grid, oponent_hit, oponent_hit.r_attack)

        if not oponent_hit.idea_ship.live:
            oponent_hit.idea = []

    else:
        if len(oponent_hit.oponents_possible_hit) != 0:
            r_attack_index = random.randint(0, len(oponent_hit.oponents_possible_hit) - 1)
            oponent_hit.r_attack = oponent_hit.oponents_possible_hit[r_attack_index]
            oponent_attack(grid, oponent_hit, oponent_hit.r_attack)
    return oponent_hit.attack, oponent_hit.r_attack


def add_miss_after_death(grid, ship, hit):
    """Отбрасывает ненужные клетки после уничтожения корабля
    Input:
        grid - объект класса Grid, который атакуется
        ship - объект класса Ship, который уничтожили
        hit - объект класса Hit, атакующего
    """
    for R in ship.r_dead:
        for m in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                for j in ship.r_dead:
                    if (R[0] + m, R[1] + k) == j:
                        hit.exist = True
                    for missed in grid.miss:
                        if (R[0] + m, R[1] + k) == missed:
                            hit.exist = True
                    if R[0] + m < 1 or R[0] + m > grid.lenght:
                        hit.exist = True
                    if R[1] + k < 1 or R[1] + k > grid.height:
                        hit.exist = True
                    if not hit.exist:
                        grid.miss.append((R[0] + m, R[1] + k))
                    if hit.exist:
                        hit.exist = False


def add_miss_after_hit(grid, hit, r):
    """Отбрасывает ненужные клетки после успешного попадания
    Input:
        grid - объект класса Grid, который атакуется
        ship - объект класса Ship, который уничтожили
        r - координата атаки"""
    for k in [-1, 1]:
        for m in [-1, 1]:
            for missed in grid.miss:
                if (r[0] + k, r[1] + m) == missed:
                    hit.add_miss_possibility = False
            if r[0] + k < 1 or r[0] + k > grid.lenght:
                hit.add_miss_possibility = False
            if r[1] + m < 1 or r[1] + m > grid.height:
                hit.add_miss_possibility = False
            if hit.add_miss_possibility:
                grid.miss.append((r[0] + k, r[1] + m))
            hit.add_miss_possibility = True


def oponent_attack(grid, hit, r):
    """Ход опонента. Проверяет есть ли по данной клетки корабль, если есть уничтожает его часть. сообщает информацию в
    hit а также grid.
    Input:
        grid - объект класса Grid, который атакуется
        ship - объект класса Ship, который уничтожили
        r - координата которую атакуют
        """
    for ship in grid.ships:
        for ship_r in ship.r_live:
            if r == ship_r:
                hit.attack = True
                hit.oponents_idea = True
                ship.r_dead.append(r)
                ship.r_live.remove(r)
                add_miss_after_hit(grid, hit, r)
                if not ship.r_live:
                    hit.oponents_idea = False
                    ship.live = False
                    add_miss_after_death(grid, ship, hit)
                    hit.idea = []
                if ship.r_live:
                    hit.idea_ship = ship
                    for k in [-1, 1]:
                        if r[0] + k < 1 or r[0] + k > grid.lenght:
                            hit.create_idea_possibility = False
                        if (r[0] + k, r[1]) in grid.miss:
                            hit.create_idea_possibility = False
                        for ships in grid.ships:
                            if (r[0] + k, r[1]) in ships.r_dead:
                                hit.create_idea_possibility = False
                        if hit.create_idea_possibility:
                            hit.idea.append((r[0] + k, r[1]))
                        hit.create_idea_possibility = True
                    for m in [-1, 1]:
                        if r[1] + m < 1 or r[1] + m > grid.height:
                            hit.create_idea_possibility = False
                        if (r[0], r[1] + m) in grid.miss:
                            hit.create_idea_possibility = False
                        for ships in grid.ships:
                            if (r[0], r[1] + m) in ships.r_dead:
                                hit.create_idea_possibility = False
                        if hit.create_idea_possibility:
                            hit.idea.append((r[0], r[1] + m))
                        hit.create_idea_possibility = True
        if not hit.attack:
            grid.miss.append(r)


def create_new_list_of_possible_blocks(grid, hit):
    """Создает новый список элементов, куда можно выстрелить (функция для опонента)
    Input:
        grid - объект класса Grid, который атакуется
        hit - объект класса Hit, атакующего
    """
    hit.new_list = []
    for i in hit.oponents_start_list:
        if not (i in grid.miss):
            for ship in grid.ships:
                if i in ship.r_dead:
                    hit.choice_posibility = False
            if hit.choice_posibility:
                hit.new_list.append(i)
            else:
                hit.choice_posibility = True
    hit.oponents_possible_hit = hit.new_list


def create_new_idea(grid, hit):
    """
    Создает новую Идею, анализируя поле, и прошлую идею.
    Input:
        grid - объект класса Grid, который атакуется
        hit - объект класса Hit, атакующего
    """
    hit.new_idea = []
    for i in oponent_hit.idea:
        if i in grid.miss:
            oponent_hit.choice_posibility = False
        for j in grid.ships:
            if i in j.r_dead:
                oponent_hit.choice_posibility = False
        if oponent_hit.choice_posibility:
            hit.new_idea.append(i)
        oponent_hit.choice_posibility = True
    oponent_hit.idea = hit.new_idea
