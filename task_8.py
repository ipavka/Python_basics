# Task 1
from datetime import datetime as dt

"""
Импортирую библиотеку datetime для проверки валидности даты
"""


class Data:

    def __init__(self, m_data):
        self.m_data = m_data

    @staticmethod
    def valid_date(m_data):
        """
        Вариант проверки валидности даты
        с помощью библиотеки datetime
        """
        try:
            dt.strptime(''.join(m_data), '%d-%m-%Y')
            return f'{m_data} Дата валидная'
        except ValueError:
            return f'{m_data} Дата невалидная!!!'

    @staticmethod
    def valid_date_2(m_data):
        """
        Простой вариант проверки валидности даты
        без учета високосного года и 30 дней в месяце
        """
        day, month, year = m_data.split('-')
        if 1 <= int(day) <= 31:
            if 1 <= int(month) <= 12:
                if 1 <= int(year) <= 2020:
                    return f'Дата валидная'
                else:
                    return f'Год введен не верно!'
            else:
                return f'Месяц введен не верно!'
        else:
            return f'День введен не верно!'

    @classmethod
    def type_date(cls, m_data):
        day, month, year = m_data.split('-')
        return f'{int(day)}, {int(month)}, {int(year)}'


print(Data.valid_date('02-08-2020'))
print(Data.valid_date_2('40-08-2020'))
print(Data.type_date('20-08-2020'))


# Task 2

class OwnDivision(Exception):

    @staticmethod
    def zero_div():
        try:
            number_1 = int(input(f'Введите делимое число: '))
            number_2 = int(input(f'Введите делитель: '))
            if number_2 == 0:
                raise OwnDivision('На ноль не делят!')
            else:
                return round(number_1 / number_2, 2)
        except ValueError:
            return f'Это не число!'
        except OwnDivision as e:
            return e


print(OwnDivision.zero_div())


# Task 3

class Error(Exception):
    def __init__(self, text):
        self.text = text


num_list = []
print(f'Для оканчания ввода введите "stop"')
while True:
    try:
        num_input = input('Введите число: ')
        if num_input.isdigit():
            num_list.append(num_input)
        elif num_input == 'stop':
            print(f'Результат ввода {num_list}')
            break
        else:
            raise Error('Это не число!')
    except Error:
        print('Это не число!')


# Task 4,5,6

class EquipHouse:
    """
    Класс Склад Оргтехники хранящий список всего оборудования.
        equip_list - список всего оборудования
    """
    equip_list = []

    def __init__(self):
        pass


class OfficeEquip:
    """
    Базовый класс всей оргтехники
    """

    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price


class Printer(OfficeEquip):
    """
    Класс наследник для Принтеров
    """

    def __init__(self, name, model, price, p_type):
        super().__init__(name, model, price)
        self.p_type = p_type
        EquipHouse.equip_list.append({
            'Название': self.name,
            'Модель': self.model,
            'Цена': self.price,
            'Особенность': self.p_type
        })


class Scanner(OfficeEquip):
    """
    Класс наследник для Сканеров
    """

    def __init__(self, name, model, price, s_type):
        super().__init__(name, model, price)
        self.s_type = s_type
        EquipHouse.equip_list.append({
            'Название': self.name,
            'Модель': self.model,
            'Цена': self.price,
            'Особенность': self.s_type
        })


class Copier(OfficeEquip):
    """
    Класс наследник для 'Ксероксов'
    """

    def __init__(self, name, model, price, c_type):
        super().__init__(name, model, price)
        self.c_type = c_type
        EquipHouse.equip_list.append({
            'Название': self.name,
            'Модель': self.model,
            'Цена': self.price,
            'Особенность': self.c_type
        })


ofice = EquipHouse()
pri_1 = Printer('HP', 'hp-100', 8000, 'лазерный')
pri_2 = Printer('Canon', 'cn-40g', 7000, 'струйный')
scan_1 = Scanner('Epson', 'v-370', 5500, 'A3')
cop_1 = Copier('Xerox', 'В-205', 8000, 'лазерный')

print(ofice.equip_list)


# Task 7

class CompNum:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)

    def __add__(self, other):
        return f'Сумма комлексных чисел: {self.a + other.a}+{self.b + other.b}i'

    def __mul__(self, other):
        return f'Произведение комлексных чисел: {self.a * other.a - (self.b * other.b)}+{self.b * other.a}i'


num_1 = CompNum(1, 2)
num_2 = CompNum(3, 1)
print(num_1.__add__(num_2))
print(num_1 * num_2)
