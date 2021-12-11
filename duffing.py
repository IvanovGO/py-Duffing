#!/usr/bin/python
from math import pi
from math import sin
from math import fabs
import numpy as np
import matplotlib.pyplot as plt

print ("Нахождение траектории движения маятника")
x  = 0.0   # начальные координаты м
v  = 0.0   # начальная скорость м/с
a  = 0.0   # начальное ускорение м/с**2
dt = 0.01 # дискретизация

m  = 1.10      # масса шара кг
ro = 7200.0     # плотность материала шара кг/м**3
r  = (3/4/pi*(m/ro))**(1/3) # расчет радиуса шара
g  = 9.8      # гравитация (уск.свобод.пад.) м/с**2
k  = 100*m*g # жесткость пружины Н/м
hs = 1.0      # высота точки подвеса м
hl = 0.5      # длинна пружины в свободном состоянии м

w = 0.15      # частота возмущающего воздействия
A = 0.0       # интенсивность  воздействия

ra = 1.21     # плотность воздуха
Ss = pi*r**2  # площадь миделя шара
Cf = 0.45     # коэффициент сопротивления воздуха для шара



def Fv(v): # сопротивление воздуха
        return Cf*ra*v*v/2*Ss #

def Fs(x): # сила реакции пружины
        el=(hs-hl)-x
#        print("el=%1.1f" % el)
        return k*el

Fg=m*g # сила тяжести

t=0 # да будет свет!

T=np.array(0) # вектор с временем
X=np.array(x) # вектор с положениями
V=np.array(v) # вектор скоростей
F=np.array(Fs(x)) # вектор реакции пружины
FU=np.array(0) #

#print ("Fv=%1.2f Fs=%1.2f Fg=%1.2f x=%1.2f a=%1.2f v=%1.2f t=%1.2f" % (Fv(v),Fs(x),Fg,x,a,v,t))              

while  t<1000.0: #бесконечный цикл
          Fu=Fv(v+A*sin(w*t)) # возмущающая сила - поток воздуха в направлении оси Х перпемнной силы
          a=(Fv(-v)+Fs(x)-Fg)/m # ускорение по закону Ньютона
          v+=a*dt   #  вычиляем скорость по ускорению
          x+=v*dt   #  вычисляем положение по скорости
          t+=dt;    #  текущее время
          T=np.append(T,t) # сохраняем результаты 
          X=np.append(X,x) #
          V=np.append(V,v) #
          F=np.append(F,Fs(x)) # 
          FU=np.append(FU,Fu) # 



fig,ax=plt.subplots() #строим графики
plt.plot(T,X,label='положение, м')
plt.plot(T,V,label='скорость, м/с')
plt.plot(T,F,label='реакц. пруж. Н')
plt.plot(T,FU,label='возм. сила Н')
plt.legend()
ax.set_xlabel('Время T, сек')
ax.set_ylabel('Величина')
print(Fg,Fs(x))

plt.show()

#print ("Fv=%1.2f Fs=%1.2f Fg=%1.2f x=%1.2f a=%1.2f v=%1.2f t=%1.2f" % (Fv(v),Fs(x),Fg,x,a,v,t))     


print("this is all folks")
