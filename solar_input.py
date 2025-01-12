# coding: utf-8
# license: GPLv3
# Пробный коммит

from os import lseek
from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXED: do the same for planet
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """
    massiv = list(line.strip().split())
    star.R = float(massiv[1])
    star.color = massiv[2]
    star.m = float(massiv[3])
    star.x = float(massiv[4])
    star.y = float(massiv[5])
    star.Vx = float(massiv[6])
    star.Vy = float(massiv[7])


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    massiv = list(line.strip().split())
    planet.R = float(massiv[1])
    planet.color = massiv[2]
    planet.m = float(massiv[3])
    planet.x = float(massiv[4])
    planet.y = float(massiv[5])
    planet.Vx = float(massiv[6])
    planet.Vy = float(massiv[7])


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(obj.type + " " + str(obj.R) + " " +
                           obj.color + " " + str(obj.m) + " " + str(obj.x) + " " +
                           str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) + "\n")
            out_file.write("\n")


def append_space_objects_stat_to_file(stat_filename, space_objects, t):
    """Добавляет новую cтатистику космических объектов в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса>:
        <t>: <x> <y> <Vx> <Vy>
        ...
    Planet <радиус в пикселах> <цвет> <масса>:
        <t>: <x> <y> <Vx> <Vy>
        ...

    Параметры:

    **stat_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    **t** - время сохранения статистики
    """
    pass #FIXME


if __name__ == "__main__":
    print("This module is not for direct call!")
