#1 задание
def divide():
    x = float(input("Введите делимое: "))
    y = float(input("Введите делитель: "))
    print(x/y) if y != 0 else print('Невозможно выполнить деление')
divide()

#2 задание
def data(name, surname, yearbirth, city, email, tel):
    print(f'{name} {surname}, {yearbirth} год рождения, г.{city}, эл. почта: {email}, тел.:{tel}')
data(name ='Иван', surname = 'Иванов', yearbirth='1979', city='Москва', email='ivanovivan@mail.ru', tel='89165381920')

#3 задание
def my_func():
    x, y, z = (float(input("Ведите число: ")) for arg in range(3))
    print(x + y + z - min(x, y, z))
my_func()
# #3 задание, если числа не запрашиваются у пользователя
# def my_func(x, y, z):
#     print(x + y + z - min(x, y, z))
# my_func(2, 3, -7)

#4 задание 1 вариант
def my_function(x, y):
    print(1/(x**abs(y)))
my_function(3, -2)
# #4 задание 2 вариант
# def my_function(x, y):
#     if (y < 0) and (x > 0) and (type(y) == int):
#         i, t = 0, 1
#         while i < abs(y):
#             t *= 1/x
#             i += 1
#         print(t)
#     else:
#         print("Введены недопустимые значения аргументов")
# my_function(3, -2)

#5 задание
def sum_string():
    summ = 0
    try:
        while True:
            for el in map(int, input().split()):
                summ += el
            print(summ)
    except ValueError:
        print(summ)
sum_string()

#6 задание
def int_func(word):
    print(word.title())
int_func("text")
# #6 задание, если запрашиваем у пользователя
# def int_func():
#     text = input('Введите строку: ').title()
#     print(text)
# int_func()