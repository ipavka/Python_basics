# Task 1
import time as t


class TrafficLight:
    """
    import time as t - модуль для тайминга запуска цветов светофора.
    color - приватный атрибут, цвета светофора.
    running - метод(функция) для запуска сфетофора.
    count - счетчик для смены очередности цветов из атрибута __color.
    while - цикл для смены цветов, после каждой итерации с увеличением count + 1.
    t.sleep - функция модуля time, для отсчета секунд ожидания.
    """
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        count = 0
        while count != 3:
            print(f'Загорелся {TrafficLight.__color[count]} цвет')
            if count == 0:
                print(f'Стоим!')
                t.sleep(7)
            elif count == 1:
                print(f'Приготовились!')
                t.sleep(2)
            elif count == 2:
                print(f'Можно ехать :)')
                t.sleep(10)
            count += 1


light = TrafficLight()
light.running()

"""
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""


# Task 2

class Road:
    """
    Класс Road с конструкроторм который принемает два аргумента
    length - длина дороги
    width - ширина дороги

    Метод calc_mass - расчитывает массу асфальта и принемает два аргумента
    для расчета покрытия одного кв метра дороги, где
    mass - масса афальта
    layer - толщина асфальта
    mass_asf - подсчет итоговой массы в тоннах (// 1000 перводим из гк. в тонны)
    """

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass(self, mass, layer):
        self.mass = mass
        self.layer = layer
        mass_asf = (self._length * self._width * self.mass * self.layer) // 1000
        print(f'Для покрытия всего дорожного полотна нужно {mass_asf} тонн асфальта')


road_to_Kursk = Road(length=5000, width=20)
road_to_Kursk.calc_mass(mass=25, layer=5)

road_to_Orel = Road(length=2000, width=20)
road_to_Orel.calc_mass(mass=20, layer=4)


# Task 3

class Worker:
    """
    Родительский класс с конструктором принемающим параметры
    name - имя сотрудника
    surname - фамилия сотрудника
    position - должность сотрудника
    _income - защищенный паремет с доходом из двух значений
            wage - оклад
            bonus -  премия
    """

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):
    """
    Класс наследник класса Worker
    get_full_name - метод для получения полного имени сотрудника
    get_total_income - метод для суммы дохода с учетом премии
    """

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


worker_1 = Position('Максим', 'Иванов', 'стажер', '30000', '5000')
worker_2 = Position('Дмитрий', 'Васильев', 'мастер', '50000', '9000')

print(f'Полное Имя сотрудника:\n'
      f'{worker_1.get_full_name()} \n'
      f'Доход с учетом премии:\n'
      f'{worker_1.get_total_income()} рублей')
print(f'{"-" * 20}') # раделитель для нагладного удобства
print(f'Полное Имя сотрудника:\n'
      f'{worker_2.get_full_name()} \n'
      f'Доход с учетом премии:\n'
      f'{worker_2.get_total_income()} рублей')

# Task 4

class Car:
    """
    Родительский класс с конструктором принемающий атрибуты(аргументы)
    name('строка') - название машины или марка ('строка')
    color('строка') - цвет машины
    speed - скорость движения
    is_police(булевое выражение) - это машина полиции?

    Методы:
    go - машина едет
    stop - машина остановилась
    turn - машина повернула, аргумент direction принемает ('строку') как направление поворота
    show_speed - провряет текущею скорость
    """

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return f'{self.name} в пути'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} повернула на {direction}'

    def show_speed(self):
        return f'Скорость машин {self.name} {self.speed} км/ч\n' \
               f'Этой машине можно так ехать :)'


class TownCar(Car):
    """
    Класс наследник от Car
    Метод show_speed - проверяет скороть на предмет превышения
    """
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости!'
        else:
            return f'Скорость в рамках ПДД'


class SportCar(Car):
    """
    Класс наследник от Car
    """
    pass


class WorkCar(Car):
    """
    Класс наследник от Car
    Метод show_speed - проверяет скороть на предмет превышения
    """
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости!'
        else:
            return f'Скорость в рамках ПДД'


class PoliceCar(Car):
    """
    Класс наследник от Car
    """
    pass


car_t = TownCar('Kia', 'белого', 65, is_police=False)
car_w = WorkCar('Maz', 'серого', 40, is_police=False)
car_s = SportCar('BMW', 'красного', 100, is_police=False)
car_p = PoliceCar('Ford', 'черного', 80, is_police=True)

"""
Для удобства вывода, пройдемся циклом по всем экземплярам
в функции print запросим все методы
"""
car_list = [car_t, car_w, car_s, car_p]

for el in car_list:
    print(f'{el.name} {el.color} цвета\n'
          f'{el.go()} \n'
          f'{el.turn("лево")}\n'
          f'{el.show_speed()}\n'
          f'{el.stop()}\n'
          f'Это машина полиции? {el.is_police}')
    print(f'{"-" * 20}') # раделитель для нагладного удобства

# Task 5


class Stationery:
    """
    Родительский Класс отрибутом title - для названия инструмента
    Метод draw - выводит запуск отрисовки
    """

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    """
    Дочерний класс от класса Stationery
    Метод draw переопределен от метода родительского Класса
    """

    def draw(self):
        return f'Пишем ручкой.'


class Pencil(Stationery):
    """
    Дочерний класс от класса Stationery
    Метод draw переопределен от метода родительского Класса
    """

    def draw(self):
        return f'Чертим карандашом.'


class Handle(Stationery):
    """
    Дочерний класс от класса Stationery
    Метод draw переопределен от метода родительского Класса
    """

    def draw(self):
        return f'Рисуем фламастером.'


"""
Создаем экземпляры классов, и в цикле for проходимся
и вызываем атрибуты и методы всех классов.
list_instance - список всех экземпляров классов.
"""

st = Stationery('Перо')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
hand = Handle('Фламастер')

list_instance = [st, pen, pencil, hand]

for el in list_instance:
    print(f'{el.title}\n'
          f'{el.draw()}')
    print(f'{"-" * 20}')  # раделитель для нагладного удобства
