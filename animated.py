import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import MaxNLocator

y_ex = [9]
y2_ex = [15]
y3_ex = [11]

values = [y_ex, y2_ex, y3_ex]
enum = [1]

# Collatz Conjecture calculation
while True:
    if y_ex[-1] == 1 and y2_ex[-1] == 1 and y3_ex[-1] == 1:
        break
    for i in values:
        if i[-1] > 1:
            if i[-1] % 2 == 0:
                i.append(i[-1] // 2)
            else:
                i.append(i[-1] * 3 + 1)
    enum.append(enum[-1] + 1)

x, x2, x3 = enum.copy(), enum.copy(), enum.copy()

while True:
    if len(y_ex) != len(x):
        x.pop(-1)
    elif len(y2_ex) != len(x2):
        x2.pop(-1)
    elif len(y3_ex) != len(x3):
        x3.pop(-1)
    else:
        break

y = y_ex
y2 = y2_ex
y3 = y3_ex


# Interpolate data
x_i = np.linspace(1, len(enum), 500)
y_i = np.interp(x_i, x, y)
y2_i = np.interp(x_i, x2, y2)
y3_i = np.interp(x_i, x3, y3)

# Plotting
fig, ax = plt.subplots()
line, = ax.plot(x_i, y_i, label=f'Starting Value: {y_ex[0]}')
line2, = ax.plot(x_i, y2_i, label=f'Starting Value: {y2_ex[0]}')
line3, = ax.plot(x_i, y3_i, label=f'Starting Value: {y3_ex[0]}')

ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=len(enum)))

def myupdating(i):
    if  y_i[-1] != y_i[i]:
        line.set_data(x_i[:i], y_i[:i])
    if y2_i[-1] != y2_i[i]:
        line2.set_data(x_i[:i], y2_i[:i])
    if y3_i[-1] != y3_i[i]:
        line3.set_data(x_i[:i], y3_i[:i])

myanimation = FuncAnimation(fig, myupdating, frames=500, interval=1)

plt.xlabel('Iteration')
plt.ylabel('Value')
plt.title('Collatz Conjecture Sequences')   
plt.legend()
plt.show()
