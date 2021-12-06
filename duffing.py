#!/usr/bin/python
from math import pi
import numpy as np
import matplotlib.pyplot as plt

print ("Нахождение траектории движения маятника")
x  = 9   # начальные координаты м
v  = 0   # начальная скорость м/с
a  = 0   # начальное ускорение м/с**2
dt = 0.0001 #

m  = 100     # масса шара кг
ro = 7200   # плотность материала шара кг/м**3
r  = (3/4/pi*(m/ro))**(1/3) # расчет радиуса шара
k  = 1000       # жесткость пружины Н/м
hs = 10     # высота точки подвеса м
hl = 3      # длинна пружины в свободном состоянии м
g  = 9.8     # гравитация (уск.свобод.пад.) м/с**2


ra = 1.21 #
Ss = pi*r**2 #
Cf = 1.05 #



def Fv(v): #
        return Cf*ra*v**2/2*Ss #

def Fs(x): # сила
        el=(hs-hl)-x
#        print("el=%1.1f" % el)
        return k*el

Fg=m*g #

t=0 #

T=np.array(0) # 
X=np.array(x) #
V=np.array(v) #
F=np.array(0) #

print ("Fv=%1.2f Fs=%1.2f Fg=%1.2f x=%1.2f a=%1.2f v=%1.2f t=%1.2f" % (Fv(v),Fs(x),Fg,x,a,v,t))              

while  t<10.0: #бесконечный цикл
          a+=(-m*a+Fs(x)-Fg-Fv(v))*dt/m #
          v+=a*dt   #
          x+=v*dt   #
          t+=dt;    #
          T=np.append(T,t) #
          X=np.append(X,x) #
          V=np.append(V,v) #
          F=np.append(F,Fs(x)) # 
          



fig,ax=plt.subplots()
plt.plot(T,X,label='положение, м')
plt.plot(T,V,label='скорость, м/с')
plt.plot(T,F,label='реакц. пруж. Н')
plt.legend()
ax.set_xlabel('Время T, сек')
ax.set_ylabel('Величина')
print(Fg,Fs(x))

plt.show()
print ("Fv=%1.2f Fs=%1.2f Fg=%1.2f x=%1.2f a=%1.2f v=%1.2f t=%1.2f" % (Fv(v),Fs(x),Fg,x,a,v,t))     
print("this is all folks")
