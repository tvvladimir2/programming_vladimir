# MATPLOTLIB


---


## Description
`Matplotlib` is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

It provides an object-oriented API for embedding plots into applications using general-purpose GUI toolkits like Tkinter, wxPython, Qt, or GTK.

`pyplot` is a state-based interface to matplotlib. It provides a MATLAB-like way of plotting.

`pyplot` is mainly intended for interactive plots and simple cases of programmatic plot generation:


## Installation
```
>> python -m pip install -U pip                          # update pip
>> python -m pip install -U matplotlib --prefer-binary   # install Matplotlib
```

---


## Graph from array of values:

![](/pictures/f_linear.png)

```python
# Import the libraries
from matplotlib import pyplot as plt

# Plot 1
x_values = [1,2,3,4]
y_values = [5,6,7,8]
plt.plot(x_values, y_values, color='navy', label='plot1')    # Shows continuos connected line values
plt.scatter(x_values, y_values) # Shows scattered values

# Plot 2
other_x_values = [1,2,3,4]  # X axis values
other_y_values = [3,2,1,5]  # Y axis values
plt.plot(other_x_values, other_y_values, color='red', label='plot2')  # Pass values to plot + add color

# Customize the plot
plt.title('The name of the plot: Godzilla!')  # Plot title
plt.xlabel('Time')    # name of X axis
plt.ylabel('Values')  # Name of Y axis
plt.legend()        # Show legend bar at the top middle with labels

# Initialize the graph
plt.show()            
```


---


## Plot a function

![](/pictures/f_quadratic.png)

```python
import matplotlib.pyplot as plt
import numpy as np

# Define a function for generating Y axis values
def function(x,a,b,c):
    return a*x**2 + b*x + c

# Define constant values
a = 3
b = 1
c = 4

# Generate lists
xlist = np.linspace(-10, 10, num=1000)   # Make a list with 1000 data points
# xlist = np.arange(-10, 10, 0.1)        # Make a list with a spacing of 0.1
ylist = function(xlist,a,b,c)

# Define a figure
# matplotlib.pyplot.figure(num=None,    # A unique identifier for the figure.
#                         figsize=None,
#                         dpi=None,     # Resolution
#                         facecolor=None,
#                         edgecolor=None,
#                         frameon=True,
#                         FigureClass=<class 'matplotlib.figure.Figure'>,
#                         clear=False,
#                         **kwargs)
plt.figure(num=0, dpi = 120)
plt.plot(xlist,ylist, color='red', label="f(x)")
plt.plot(xlist,ylist**(1/2), color='blue', '--', label=r"f(x)$^{0.5}$")

# Customize the plot
plt.title('The name of the plot: Godzilla!')  # Plot title
plt.xlabel('Input size')    # name of X axis
plt.ylabel('Time')  # Name of Y axis
plt.legend()        # Show legend bar at the top middle with labels

plt.show()
```


---
