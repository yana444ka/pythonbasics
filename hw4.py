import random as r
from functools import reduce

# 1 задание
from sys import argv

script_name, wage, labour, bonus = argv
print('Name of script:', script_name)
print('Wage: ', wage)
print('Hours worked: ', labour)
print('Bonus: ', bonus)
salary = int(wage) * int(labour) + int(bonus)
print('Salary:', salary)

# 2 задание
# если список не задан
# alist = [r.randint(-300,300) for i in range(r.randint(0,20))]
alist = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_alist = [el for i, el in enumerate(alist) if alist[i] > alist[i-1]]
print('Задание №2', f'Исходный список: {alist}', f'Новый список: {new_alist}', sep='\n')
#решение не предусматривает вариант, когда в списке 1 элемент

# 3 задание
print('Задание №3', f'Итоговый список: {[i for i in range(20,241) if i % 20 == 0 or i % 21 == 0]}')

# 4 задание
list1 = [r.randint(-300,300) for i in range(r.randint(0,20))]
list2 = [list1[i] for i in range(len(list1)) if list1.count(list1[i]) == 1]
print('Задание №4', f'Исходный список: {list1}', f'Новый список: {list2}', sep='\n')

# 5 задание
my_list = [i for i in range(100,1001,2)]
def prod(prev_el, el):
    return prev_el * el
print('Задание №5', reduce(prod, my_list), sep='\n')

# 6 задание
from itertools import count, cycle
print('Задание №6')
x = int(input('Введите число: '))
def gen_a(x):
    for i in count(x):
        if(i == x + 20):
            break
        print(i)
gen_a(x)

list = input('Введите список: ').split(' ')
k = int(input('Сколько раз повторить список? '))

def gen_b(list):
    i = 0
    for el in cycle(list):
        if el == list[0]:
            i += 1
        if i <= k:
            print(el)
gen_b(list)


# 7 задание
n = int(input('Введите число: '))
def fact(n):
    a = 1
    for i in count(1):
        if i <= n:
            a *= i
            print(a)
fact(n)
