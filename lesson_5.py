# Task 1

name = input(f'Введите имя название файла в формате имя.txt > ')
with open(name, 'w') as f:
    while True:
        print(f'Для оканчания ввода введите пустую строку')
        some_str = input(f'Введите данные: ')
        if some_str == '':
            break
        f.write(f'{some_str} \n')

# Task 2

with open('task_2.txt', 'r') as f:
    line = f.readlines()
    count = 0
    for i, el in enumerate(line):
        count += 1
        sum_world = len(el.split())
        print(f'В строке №{i + 1} кол-во слов {sum_world}')
    print(f'Колличество строк в файле > {count}')

# Task 3

with open('task_3.txt', 'r', encoding="utf-8") as f:
    content = f.read().split('\n')  # Читаем файл, убираем отступы
    count = 0  # Счетчик для общего фонда зарплаты
    num = 0  # Счетчик для количества работником
    les_tax = []  # Список для зарплаты меньше 200000
    for el in content:
        date = el.split()
        count += int(date[1])
        num += 1
        if int(date[1]) < 20000:
            les_tax.append(date[0])
    print(f'Среднея велечина доходов сотрудников {count // num}')
    print(f'Меньше 20000 зарабатывают > {", ".join(les_tax)}')

# Task 4

with open('task_4.txt', 'r', encoding="utf-8") as f:
    line_str = f.readlines()
    new_list = []
    rus_list = ['один', 'два', 'три', 'четыре']
    for i, el in enumerate(line_str):
        sm_srt = el.split()[1:]
        new_list.append(f'{rus_list[i]} {" ".join(sm_srt)}')

with open('task_4_w.txt', 'w', encoding="utf-8") as f_w:
    for elm in new_list:
        f_w.write(elm + '\n')

# Task 5

with open('task_5.txt', 'w', encoding="utf-8") as f:
    int_str = input(f'Введите числа через пробел: ')
    f.writelines(int_str)
with open('task_5.txt', 'r', encoding="utf-8") as f_r:
    num_str = f_r.readline().split()
    # решение с помощью функции map
    print(f'Сумма введенных чисел равна {sum(map(int, num_str))}')
    # решение с помощью цикла и функции sum
    int_str = []
    for i in num_str:
        int_str.append(int(i))

    print(f'Сумма введенных чисел равна {sum(int_str)}')

# Task 6

my_dict = {}
with open('task_6.txt', 'r', encoding="utf-8") as f:
    lin_list = f.read().split('\n')[:-1]
    for item in lin_list:
        key = item.split(' ')[0]
        value = item.split(' ')[1:]
        count = ''
        sum_count = []
        for i in ' '.join(value):
            if i.isdigit():
                count = count + i
            else:
                if count != '':
                    sum_count.append(int(count))
                    count = ''
        my_dict[key] = sum(sum_count)
    print(my_dict)

# Task 7

import json

firm_dict = {}
profit = {'average_profit': None}
profit_firm = {}
loss_firm = {}
total_list = []
with open('task_7.txt', 'r', encoding="utf-8") as f:
    firm_list = f.read().split('\n')[:-1]
    num = 0
    for n, firm in enumerate(firm_list):
        key = firm.split(' ')[0]
        value = firm.split(' ')[2:]
        num = n
        firm_dict[key] = int(value[0]) - int(value[1])
    med_prof = 0
    for k, v in firm_dict.items():
        if v < 0:
            print(f'{k} сработала с у убытком {abs(v)}')
            num -= 1
            loss_firm[k] = v
        else:
            print(f'Прибыль {k} составила {v}')
            med_prof += v
            profit_firm[k] = v
    profit['average_profit'] = med_prof // (num + 1)
    total_list.extend([profit_firm, loss_firm, profit])
    print(f'Среднея прибыль всех фирм с доходом равна {med_prof // (num + 1)}')
    print(total_list)

with open('task_7.json', 'w') as file_js:
    json.dump(total_list, file_js)
