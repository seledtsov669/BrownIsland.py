from turtle import penup, pendown, goto, done, speed
from random import random
from math import sqrt

def brown (x0, y0, x1, y1, disp, p, n=8, m=400):
     ''' Рекурсивная функция построения Броуновского моста.
     Параметры:
     x0, y0, x1, y1 - координаты двух точек
     disp -дисперсия
     p - плавность
     n - глубина рекурсии
     m - масштаб

     xm, ym - координаты середины
     delta - смещение
     '''
     if n==0:
          penup()
          goto(x0 * m - m / 2, y0 * m - m / 2)
          pendown()
          goto(x1 * m - m / 2,y1 * m - m / 2)
          return
     xm=(x0 + x1) / 2.0
     ym=(y0 + y1) / 2.0
     delta0 = random() * sqrt(disp)
     delta1 = random() * sqrt(disp)
     brown(x0, y0, xm + delta0, ym + delta1, disp / p, p, n-1)
     brown(xm + delta0, ym + delta1, x1, y1, disp / p, p, n-1)

def main():
     h=float(input('Показатель Херста: '))
     a = 2.0 ** (2.0 * h)
     speed(997)
     brown(0.0, 0.0, 0.0, 0.0, 0.4, a)
     done()


if __name__ == '__main__':
    main()