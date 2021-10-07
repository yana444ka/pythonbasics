# 1 задание
class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract_data(cls):
        try:
            day, month, year = self.date.split("-")
            return int(day), int(month), int(year)
        except Exception:
            print(f'Неверный формат даты')

    @staticmethod
    def validate_date(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError('Неверный формат даты (день)')
            elif month not in range(1, 13):
                raise ValueError('Неверный формат даты (месяц)')
            elif year < 0:
                raise ValueError('Неверный формат даты (год)')
        except ValueError:
            print(ValueError)


some_date = Date('7-10-2024')
print(some_date.extract_data())


# 2 задание
class MyError(Exception):

    def __init__(self):
        self.txt = 'Произошло деление на 0'


def div(a, b):
    try:
        if b == 0:
            raise MyError
        print(a / b)
    except MyError as s:
        print(s.txt)


div(1, 0)


# 3 задание
class MyException(Exception):
    def __init__(self):
        self.txt = 'Некорректный тип данных'


mylist = []
input_string = input('Введите число: ')
while input_string:
    try:
        if input_string.isdigit():
            mylist.append(int(input_string))
        else:
            raise MyException
    except MyException as e:
        print(e.txt)

    input_string = input('Введите число: ')

print(mylist)


# 4,5,6 задание
def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print('Недостаточно техники на складе')
        except KeyError:
            print("Нет такого типа оргтехники на складе!")

    return wrapper


class Storage:
    """
    equipment_units имеет следующую структуру
    equipment_units = {
    "equipment_type": {
    "name": {
    "model": {
    "count": ""
    }
    }
    }
    }
    """
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]["count"] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]["count"]
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]["count"] -= unit_count

    @staticmethod
    def get_all_equipment():
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) not in [int, float]:
                self.__count = 0
                raise ValueError
        except ValueError:
            print("Неверный формат входных данных!")
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model["count"] += self.__count
            else:
                equipment_storage_info_by_name[self.model] = {"count": self.__count}
        else:
            equipment_storage_info[self.name] = {
                self.model: {"count": self.__count}
            }

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, "Printer", count)
        self.colors = colors


class Notebook(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, "Notebook", count)
        self.ram = ram
        self.system_type = system_type


# 7 задание
class Complex:
    def __init__(self, x, y):
        self.x = x  # действительная часть
        self.y = y  # мнимая часть

    def __str__(self):
        return f"{self.x} + {self.y}i"

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


z1 = Complex(1, -1)
z2 = Complex(2, 3)
print(z1 + z2, z1 * z2, sep='\n')
