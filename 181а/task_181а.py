__autor__ = 'Райков'
'''
181 Даны целые числа a1,...a50.
Получить сумму тех чисел данной последовательности, которые
а)кратные 5
'''

from unit_181а import Class181 as unit

if __name__ == '__main__':
    n = int(input("введите n\n"))

    u = unit(n)  # создаем объект класса Class181
    u.print_arr()  # вывод массива
    # вывод результата
    print(f'сумма равна = {u.logic():.3f}')
