import numpy as np
import matplotlib.pyplot as plt

def system_of_equations(x, y):
    """
    Define the system of first-order differential equations.
    dx/dt = f(x, y)
    dy/dt = g(x, y)
    """
    dx_dt = 3*x + -2*y
    dy_dt = 4*x + -1*y
    return dx_dt, dy_dt

# Define the range and number of points for plotting
x_range = np.linspace(-2, 2, 20)
y_range = np.linspace(-2, 2, 20)


# Create a grid of initial conditions
X, Y = np.meshgrid(x_range, y_range)

# Calculate the derivatives at each point in the grid
DX, DY = system_of_equations(X, Y)


# Plot the phase portrait
plt.figure(figsize=(8, 6))
plt.streamplot(X, Y, DX, DY, density=2.0, arrowsize=1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(-2,2)
plt.title('Phase Portrait of the System')
plt.grid()
plt.show()

            
            
            
    
    
    