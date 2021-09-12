#1 задание
x = 2
a = True
b = 'name'
print(x, a, b)
z = int(input())
m = float(input())
text = input()
text_second = input()
print (z, m, text, text_second)

#2 задание
time = int(input("Введите количество секунд:"))
hours = time//3600
minutes = (time - hours*3600)//60
seconds = time - hours*3600 - minutes*60
print(f'{hours}:{minutes}:{seconds}')

#3 задание
my_number = int(input("Ведите число:"))
smy_number = str(my_number)
print(my_number + int(smy_number*2) + int(smy_number*3))

#4 задание
my_number = input("Введите число:")
gr = -1
i = 0
while i < len(my_number):
    if int(my_number[i]) > gr:
        gr = int(my_number[i])
    i += 1
print(gr)

#5 задание
tr = float(input("Выручка:"))
tc = float(input("Издержки:"))
pr = tr - tc
if pr > 0:
    print(f"Ваша фирма прибыльна. Рентабельность выручки составляет {pr/tr}")
elif pr < 0:
    print("Ваша фирма убыточна")
empl = int(input("Количество работников:"))
print(f"Прибыль фирмы в расчете на одного сотрудника: {pr/empl}")

#6 задание
a = int(input())
b = int(input())
t = 1
while a < b:
    t += 1
    a *= 1,1
print(t)