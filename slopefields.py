
import numpy as np
from matplotlib import pyplot as plt

# purpose: plot direction (slope) fields of a differential equation
# y' = f(t, y)

def ode_rhs(t, y): # define the right side f(t,y) = y*(y-2)
    f = y*(y-2) 
    return f

t = np.linspace(-5,5,15) # the range of t values [-5,5] at 15 points
y = np.linspace(-2,4,15) # the range of y values [-2,4] at 15 points
T,Y = np.meshgrid(t,y) # create a grid of the t-y values
DT = np.ones_like(T)
DY = ode_rhs(T,Y)
S = (DT**2+DY**2)**0.5
plt.figure()
plt.xlabel(r'$t$')
plt.ylabel(r'$y(t)$')
plt.quiver(T, Y, DT/S, DY/S, angles='xy', color='b') # plot direction field arrows
plt.grid()






