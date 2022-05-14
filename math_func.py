""" Модуль для математических функций """
from math import sqrt

def cube(a):
""" Вычисляет объем куба с ребром a и возвращает его в качестве результата"""
    return a*a*a

def Heron(a, b, c):
    p = (a+b+c)/2

    return sqrt((p-a)*(p-b)*(p-c))
def hipot(a, b):
""" Вычисляет гипотенузу треугольника по катетам и возвращает в качестве 
результата"""
    return sqrt(a*a +b*b)

if __name__=='__main__':
    print('Вызов',__name__)
