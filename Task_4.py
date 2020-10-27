# Task 1
from sys import argv

try:

    script_name, work_hour, hour_rate, bonus = argv


    def calc_pay():
        result = int(work_hour) * int(hour_rate)
        return f'Заработная плата сотрудника : {int(result) + int(bonus)} рублей'


    print(calc_pay())


except ValueError:  # обрабатываем ошибку ввода кол-во параметров
    print(f'Введите 3 параметра: 1. Часы работы'
          f' 2. Ставка оклада в час'
          f' 3. Размер премии')

# Task 2
"""
Два варианта решения, первый с помощию нумерации, второй с помощью функции zip
"""
or_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
sort_list = [el for num, el in enumerate(or_list) if or_list[num - 1] < or_list[num]][1:]

sort_list_2 = [el for i, el in zip(or_list, or_list[1:]) if el > i]

print(or_list)
print(sort_list)
print(sort_list_2)

# Task 3

lis_1 = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]


print(lis_1)

# Task 4

numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = [i for i in numbers if numbers.count(i) == 1]

print(result)

# Task 5

from functools import reduce

my_list = reduce(lambda x, y: x * y, [i for i in range(100, 1001) if i % 2 == 0])

print(my_list)

# Task 6

from itertools import count, cycle

#  итератор, генерирующий целые числа, начиная с указанного

num = int(input(f'Введите стартовое число >>> '))
for el in count(num):
    if el > 10:
        break
    else:
        print(el)
#  итератор, повторяющий элементы определенного списка

some_list = ['test', 'some', 'text']

num = 0
for i in cycle(some_list):
    if num > 15:
        break
    num += 1
    print(i.title(), end=' ')

# Task 7


def fact(num):
    num_temp = 1
    for i in range(1, num + 1):
        num_temp *= i
        yield num_temp


for el in fact(4):
    print(el, end=' ')
