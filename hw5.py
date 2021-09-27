#1 задание
with open('new_file', 'w+') as file_1:
    string = input()
    while string != "":
        file_1.write(string + '\n')
        string = input()

#2 задание
with open('a_file', 'r') as file_2:
    i = 0
    for line in file_2:
        i += 1
    print(i)

#3 задание
with open('data', 'r') as file_3:
    sum = 0
    n = 0
    for line in file_3:
        surname, salary = line.split(' ')
        sum += int(salary)
        n += 1
        if int(salary) < 20000:
            print(line, end='')
print('Средняя з/п: ', sum/n)

#4 задание
my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('one_more_file', 'r') as file_eng, open('one_more_file_rus', 'w') as file_rus:
    for line in file_eng:
        if line != '\n':
            i = line.find(' ')
            file_rus.write(my_dict[line[:i]] + line[i:] + '\n')
        else:
            print(line)

#5 задание
my_list = input("Введите числа: ")
summ = 0
with open('my_file', 'w+') as file_5:
    file_5.write(my_list)
    for el in my_list.split(' '):
        summ += int(el)
print(f'Сумма: {summ}')

#6 задание
my_keys = []
my_values = []
with open('subjects', 'r') as file_6:
    for line in file_6:
        line = line.replace('(пр)', '')
        line = line.replace('(лаб)', '')
        line = line.replace('(л)', '')
        line = line.replace('\n', '')
        my_keys.append(line[:line.find(':')])
        sums = 0
        for el in line[(line.find(':') + 2):].split(" "):
            if el != '—':
                sums += int(el)
        my_values.append(sums)
print(dict(zip(my_keys, my_values)))

#7 задание
import json
my_keys = []
my_values = []
i, sum_p = 0, 0
with open('firms_data', 'r') as file_7, open('firms_data_json', 'w+') as file_json:
    for line in file_7:
        my_keys.append(line.split(' ')[0])
        profit = int(line.split(' ')[2]) - int(line.split(' ')[3])
        my_values.append(profit)
        if profit >= 0:
            i += 1
            sum_p += profit
    summary = [dict(zip(my_keys, my_values)), {'average profit': sum_p/i}]
    json.dump(summary, file_json)

