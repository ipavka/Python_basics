#  Task 1

def divis_num(num_1, num_2):
    """
    Функция принемает два позиционных аргумента, числа и делит их.
    Функция обрабатывает ошибку деления на 0
    :param num_1: число делимое
    :param num_2: число делитель
    :return: возвращает результат деления двух чисел.
    """
    try:
        return round(num_1 / num_2, 2)
    except ZeroDivisionError:
        return f'На ноль делить нельзя!'
    except TypeError:
        return f'Введите число!'


def ask_numbers():
    """
    Функция запрашивает у пользователя числа
    проверет верность ввода и направляет их в другоую функцию divis_num для обработки
    :return: передает два числа как параметры в функцию divis_num
    """
    try:
        num1 = int(input(f'Введите превое число: '))
        num2 = int(input(f'Введите второе число: '))
        print(divis_num(num1, num2))
    except ValueError:
        print(f'Введите число!')


ask_numbers()


# Task 2

def about_user(**kwargs):
    """
    Функция принемает именованные параметры пользователя и
    возвращает данные одной строкой.
    :param kwargs: принемает не ограниченное кол-во именованых параметров
    :return: возвращает введенные данные одной строкой
    """
    pri_li = list(kwargs.values())
    pri_str = ', '.join(map(str, pri_li))
    return pri_str


print(about_user(name='Max', surname='Kotov', birth=1985, city='Kursk', email='max@ya.ru', tel=4582863))


# Task 3

def sum_nuber(num_1, num_2, num_3):
    """
    Функция принемает на вход 3 числа
    и возвращает сумму двух наибольших.
    :param num_1: любое число
    :param num_2: любое число
    :param num_3: любое число
    :return: возвращает сумму двух наибольших чисел
    """
    lis_num = sorted([num_1, num_2, num_3])
    lis_num.remove(lis_num[0])
    return sum(lis_num)


print(sum_nuber(8, 10, 12))


# Task 4

def degree(x, y):
    """
    Функция возведения в степень с помощью **
    :param x: число возводимое в степень
    :param y: число множетель степени
    :return: результат возведение в степень
    """
    return x ** y


print(degree(5, -2))


def degree_cycle(x, y):
    """
    Функция возведения в степень с помощью цикла,
    Если множетель отрицательный, возвращает другой ответ.
    :param x: число возводимое в степень
    :param y: число множетель степени
    :return: результат возведение в степень
    """
    if y < 0:
        y = abs(y)
        multi = 1
        while y > 0:
            multi = multi * x
            y = y - 1
        return 1 / multi
    else:
        multi = 1
        while y > 0:
            multi = multi * x
            y = y - 1
        return multi


print(degree_cycle(5, -2))


# Task 5

def my_sum():
    """
    Функция принимает строку из цифр, через пробел
    :return: возращает сумму этих числе
    """
    print(f'Вводите числа через пробел или > ! < для выхода')
    result = 0
    while True:
        str_number = input(f'Введите числа через пробел >>> ')
        sum_number = str_number.split()
        for num in sum_number:
            try:
                if num == '!':
                    print(f'{result}')
                    return
                else:
                    result += int(num)
            except ValueError:
                print(f'Неверный ввод! Введите число или > ! < для выхода!')
        print(f'{result}')


my_sum()


# Task 6

def int_func(*args):
    """
    Функция принемает строку из слов в нижнем регистре,
     и возвращает ее с каждым словом с большой буквы
    :param args: принемает список слов рпзделеных пробелом
    :return: возвращает список в иде строки
    """
    arg_str = ' '.join(args)
    arg_list = arg_str.split()
    st = []
    for i in arg_list:
        st.append(i.capitalize())
    return ' '.join(st)


print(int_func('text test some else'))
