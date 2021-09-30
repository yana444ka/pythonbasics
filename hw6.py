#1 задание
from itertools import cycle
from time import sleep
class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(self):
        lights = ('red', 'yellow', 'green')
        lags = (7, 2, 9)
        lights_cycle = cycle(lights)
        for el in lights:
            if el == self.__color:
                print(lights.index(self.__color))
                sleep(lags[lights.index(self.__color)])
                self.__color = next(lights_cycle)


#2 задание
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_weight(self, weight, thickness):
        print(self._length * self._width * weight * thickness)

#3 задание
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
        return {self._income["wage"] + self._income["bonus"]}

#4 задание
class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
