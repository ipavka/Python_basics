# Task 1
a = 777
b = 'lucky number'
print(a)
print(b)
print(f'{b} = {a}')

today_str = input('Какой сейчас месяц? : ')
bth_str = input('В каком месяце у тебя день рождение? : ')
today_in = int(input('Какой сегодня год? : '))
bth_in = int(input('В каком году у тебя день рождение? : '))

print(f'На дворе {today_str} месяц')
print(f'А в месяце {bth_str} ты родился')
print(f'Сейчас {today_in} год')
print(f'Ты родился в {bth_in} году')

# Task 2
time = int(input('Введите время в секундах, желательно, четырехзначное число :) : '))
hour = (time // 60) // 60
minutes = time // 60
seconds = time % 60
print(f'{"%02d" % hour}:{"%02d" % (minutes - hour * 60)}:{"%02d" % seconds}')

# Task 3
n = input('Введите число : ')
sum_n = int(n) + int(n * 2) + int(n * 3)
print(sum_n)

# Task 4
pass    # no idea how to do this task

# Task 5
revenue = int(input('Сколько заработали? > '))
expense = int(input('Сколько потратили? > '))
profit = revenue - expense
margin = profit / expense
if revenue > expense:
    print(f'Фирма доходная, выручка состовляет {profit} руб')
    print(f'Рентабельность выручки, составила {int(margin * 100)}%')
    staff = int(input('Сколько сотрудников на фирме? > '))
    print(f'Чистая прибыль на каждого работника фирмы составляет {profit // staff} руб')
else:
    print(f'Что то пошло не так, нужен новый фин. дир. или инвесторы :)')

# Task 6
a = 2
b = 3
count = 0
while True:
    count += 1
    print(f'{count}-й день: {round(a, 2)} км. ')
    a += (a * 0.1)
    if a >= b:
        print(f'{count + 1}-й день: {round(a, 2)} км. ')
        print(f'На {count + 1}-й день спортсмен достиг результата — не менее {int(a)} км.')
        break














