import numpy as np
import matplotlib.pyplot as plt
from math import sin  as sin
from math import pi  as pi
def f(x):
        y =  [] 
        for a in x :
                    y.append(sin(a))
        return y




x = np.linspace ( start = 0.    # lower limit
                , stop =  6*pi     # upper limit
                , num = 180      # generate 51 points between 0 and 3
                )
y = f(x)    # This is already vectorized, that is, y will be a vector!
plt.plot(x, y)
plt.show()

