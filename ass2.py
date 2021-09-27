#1 задание
my_list = [1, 'hello', 3.5, True]
for i in range(len(my_list)):
    print(type(my_list[i]))

#2 задание
new_list= [int(s) for s in input().split()]
for i in range (1,len(new_list),2):
    t = new_list[i-1]
    k = new_list[i]
    new_list[i-1] = k
    new_list[i] = t
print(' '.join([str(i) for i in new_list]))

#3 задание
seasons = ['Winter', 'Spring', 'Summer', 'Fall', 'Winter']
t = int(input('Ведите число от 1 до 12:'))
k = t//3
print(seasons[k])
match_seasons = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Fall': [9, 10, 11]}
for key, val in match_seasons.items():
    for i in val:
        if i == t:
            print(key)

#4 задание
alist = str(input()).split(" ")
for i in range(len(alist)):
    if len(alist[i]) <= 10:
        print(i, alist[i])
        i += 1
    else:
        print(i, alist[i][:11])
        i += 1

#5 задание
my_list = []
length = int(input())
for i in range(length):
    a = int(input())
    my_list.append(a)
    my_list.sort(reverse=True)
    i += 1
print(my_list)

#6 задание
q = int(input("Введите количество товаров:"))
names_list = []
prices_list = []
quantity_list = []
metrics_list = []
my_dict = {
    'название': names_list,
    'цена': prices_list,
    'количество': quantity_list,
    'ед': metrics_list
}
for i in range(q):
    names_list.append(input('название'))
    prices_list.append(float(input('цена')))
    quantity_list.append(float(input('количество')))
    metrics_list.append(input('ед'))
    new_dict = {
    'название': names_list[i],
    'цена': prices_list[i],
    'количество': quantity_list[i],
    'ед': metrics_list[i]
    }
    print(tuple([i+1, new_dict]))
print(my_dict)