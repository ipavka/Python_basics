# Task 1
list_diff_elem = [34, 'abc', 45.5, True, None, [], (), {}]
for elements in list_diff_elem:
    print(f'Элемент "{elements}" является типом данных {type(elements)}')

# Task 2
elem = input('Введите элементы списка через пробел : ')
elem_list = elem.split()
count = 0

for i in range(len(elem_list) // 2):  # Делим на 2 без остатка, что бы пройтись по каждому второму элементу
    elem_list[count], elem_list[count + 1] = elem_list[count + 1], elem_list[count]
    count += 2
print(elem_list)

# Task 3

seas_list = ['Зима', 'Весна', 'Лето', 'Осень']

seasons = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}

month = int(input('Введите месяц в виде целого числа от 1 до 12 : '))

if month == 1 or month == 2 or month == 12:
    print(f'Это {seas_list[0]} < ответ из списка')
    print(f'Это {seasons[1]} < ответ из словаря ')
elif 3 <= month <= 5:
    print(f'Это {seas_list[1]} < ответ из списка')
    print(f'Это {seasons[2]} < ответ из словаря ')
elif 6 <= month <= 8:
    print(f'Это {seas_list[2]} < ответ из списка')
    print(f'Это {seasons[3]} < ответ из словаря ')
elif 9 <= month <= 11:
    print(f'Это {seas_list[3]} < ответ из списка')
    print(f'Это {seasons[4]} < ответ из словаря ')
else:
    print(f'Нет такого месяца... > {month} <')

# Task 4
user_str = input("введите строку ")
list_print = user_str.split(' ')

for i in range(len(list_print)):
    print(i + 1, ''.join(list_print[i][0:10]))

for i, elem in enumerate(list_print, 1):  # вариант с методом enumerate()
    print(i, elem[0:10])

# Task 5

my_list = [7, 5, 3, 3, 2]
digit = int(input("Введите число: "))
my_list.append(digit)
my_list.sort(reverse=True)

print(my_list)

# Task 6
# Не совсем понял, что нужно сдлеать :(
