# 1 задание
class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        v = ''
        for j in self.list_of_lists:
            for i in j:
                v += f'{i}\t'
            v += '\n'
        return v

    def __add__(self, other):
        if len(self.list_of_lists) != len(other.list_of_lists):
            print('Сложение матриц невозможно')
        else:
            v = ''
            c = 0
            for j, k in self.list_of_lists, other.list_of_lists:
                for i, t in j, k:
                    c = int(i) + int(t)
                    v += f'{c}\t'
                v += '\n'
            return v


my = Matrix([[1, 2], [3, 4]])
your = Matrix([[5, 6], [7, 8]])
print(my)
print(my + your)

# 2 задание
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, x):
        self.x = x

    @abstractmethod
    def get_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, x):
        super().__init__(x)
        print(f'Пальто размера {self.x}')

    @property
    def get_consumption(self):
        return self.x / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, x):
        super().__init__(x)
        print(f'Костюм размера {self.x}')

    @property
    def get_consumption(self):
        return 2 * self.x + 0.3


a_coat = Coat(36)
a_suit = Suit(1.7)
print(
    f'Расзод ткани для пальто: {a_coat.get_consumption}, для костюма: {a_suit.get_consumption} \nИтого: {a_coat.get_consumption + a_suit.get_consumption}')
print(Clothes.__dict__)


# 3 задание
class Cell:
    def __init__(self, n):
        try:
            if n < 0:
                raise ValueError('Количество клеток не может быть меньше 0')
            self.n = int(n)
        except TypeError:
            self.n = 0
            print('Check num value')
        except ValueError:
            print('Check num value')
            self.n = 0

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        if self.n - other.n > 0:
            return Cell(self.n - other.n)
        else:
            print('Количество клеток не может быть меньше 0')

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(self.n // other.n)

    def make_order(self, k):
        return (('*' * k) + '\n') * (self.n // k) + '*' * (self.n % k)


a_cell = Cell(15)
b_cell = Cell(10)
print(a_cell.make_order(4))
