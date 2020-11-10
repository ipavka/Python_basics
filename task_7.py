# Task 1

class Matrix:

    def __init__(self, numb_list):
        self.numb_list = numb_list

    def __str__(self):
        return '\n'.join(map(str, self.numb_list))

    def __add__(self, add_list):
        for i in range(len(self.numb_list)):
            for el in range(len(add_list.numb_list[i])):
                self.numb_list[i][el] = self.numb_list[i][el] + add_list.numb_list[i][el]
        return Matrix.__str__(self)


m_1 = Matrix([[4, 2, 7, 11], [2, 4, 7, 11], [7, 11, 4, 2], [11, 2, 7, 4]])
m_2 = Matrix([[2, 0, 2, 5], [5, 3, 7, 8], [0, 3, 9, 2], [7, 3, 7, 5]])

print(m_1 + m_2)

# Task 2

from abc import ABC, abstractmethod


class Cloth(ABC):

    def __init__(self, parametr):
        self.parametr = parametr

    @property
    def Expense(self):
        pass

    @abstractmethod
    def abstract_method(self):
        pass


class Coat(Cloth):
    def consumption(self):
        sum_coat = round(self.parametr / 6.5 + 0.5, 2)
        return f'{sum_coat} м.кв. ткани для изготовления пальто.'

    def abstract_method(self):
        return 'Абстрактный метод Coat'


class Suit(Cloth):
    def consumption(self):
        sum_suit = round(2 * self.parametr + 0.3, 1)
        return f'{sum_suit} м.кв. ткани для изготовления кастюма.'

    def abstract_method(self):
        return 'Абстрактный метод Suit'


coat = Coat(44)
suit = Suit(1.65)

print(coat.consumption())
print(suit.consumption())
print(coat.abstract_method())
print(suit.abstract_method())


# Task 3

class Cell:

    def __init__(self, quant):
        self.quant = int(quant)

    def __add__(self, other):
        result = self.quant + other.quant
        return f'Клетка увеличелась до {result}'

    def __sub__(self, other):
        result = self.quant - other.quant
        return f'Клеточка уменьшилась до {result}х' if result > 0 else 'Клетки нет совсем'

    def __mul__(self, other):
        result = self.quant // other.quant
        return f'Клетка разделилась и стала {result}'

    def __truediv__(self, other):
        result = self.quant * other.quant
        return f'Клетка умножиласть и стала {result}'

    def make_order(self, row_cell):
        result = ''
        for i in range(int(self.quant / row_cell)):
            result += f'{"*" * row_cell}\\n'
        result += f'{"*" * (self.quant % row_cell)}'
        return result


c_1 = Cell(15)
c_2 = Cell(12)
print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print(f'{"-" * 20}')
print(c_1.make_order(5))
print(c_2.make_order(5))
