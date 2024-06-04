import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Function to plot a 3D graph
def plot_3d_function(func, x_range, y_range):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('3D Function Plot')

    # Adjust the viewing perspective
    ax.view_init(elev=20, azim=30)

    plt.show()

# Get a user-defined function and convert it to a callable Python function
def get_user_function():
    expression = input("Enter a multivariable function using 'x' and 'y': ")
    x, y = sp.symbols('x y')
    func = sp.lambdify((x, y), sp.sympify(expression), 'numpy')
    return func

# Define the range for x and y values
x_range = (-5, 5)
y_range = (-5, 5)

# Get user-defined function and plot it
user_function = get_user_function()
plot_3d_function(user_function, x_range, y_range)
