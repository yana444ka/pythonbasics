# 1 задание
from itertools import cycle
from time import sleep


class TrafficLight:
    lights = ('red', 'yellow', 'green')
    lags = (7, 2, 9)

    def __init__(self, color):
        self.__color = color

    def running(self):
        lights_cycle = cycle(self.lights)
        for el in self.lights:
            if el == self.__color:
                print(self.__color)
                sleep(self.lags[self.lights.index(self.__color)])
                self.__color = next(lights_cycle)


one_tl = TrafficLight('red')
one_tl.running()


# 2 задание
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, weight, thickness):
        print(f"{self._length * self._width * weight * thickness} кг")

my_road = Road(20, 5000)
my_road.asphalt_weight(25, 5)

# 3 задание
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


first_man = Position('Ivan', 'Ivanov', 'manager', 100000, 50000)
second_man = Position('Peter', 'Petrov', 'programmer', 150000, 70000)

print(first_man. get_full_name(), first_man.get_total_income())
print(second_man.get_full_name(), second_man.get_total_income())

# 4 задание
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала.')

    def stop(self):
        self.speed = 0
        print('Машина остановилась.')

    def turn(self, direction):
        print(f'Машина повернула {direction}.')

    def show_speed(self):
        print(f'Текущая скорость автомобиля: {self.speed} км/ч.')

class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = False)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости. Допустимая скорость не превышает 60 км/ч. Ваша скорость: {self.speed} км/ч.')
        else:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч.')

class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости. Допустимая скорость не превышает 40 км/ч. Ваша скорость: {self.speed} км/ч.')
        else:
            print(f'Текущая скорость автомобиля: {self.speed} км/ч.')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police = True)

class SportCar(Car):

    def __init__(self, speed, color, name, max_speed):
        super().__init__(speed, color, name, is_police = False)
        self.max_speed = max_speed

a_towncar = TownCar(120, 'Silver', 'Toyota Camri')
a_towncar.show_speed()
a_towncar.turn('налево')
a_towncar.show_speed()

a_sportcar = SportCar(200, 'Black', 'McLaren F1', 386)
a_sportcar.show_speed()
a_sportcar.turn('направо')

a_workcar = WorkCar(40, 'Yellow', 'Kia Rio')
a_workcar.show_speed()

a_policecar = PoliceCar(60, 'Blue', 'Ford Focus')
a_policecar.stop()
a_policecar.show_speed()


# 5 задание
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки. Ручка')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки. Карандаш')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки. Маркер')


brush = Stationery('paintbrush')
brush.draw()

a_pen = Pen('pen')
a_pen.draw()

a_pencil = Pencil('pencil')
a_pencil.draw()

a_handle = Handle('handle')
a_handle.draw()
