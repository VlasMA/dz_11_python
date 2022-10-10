# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30
# Определить корни
# Найти интервалы, на которых функция возрастает
# Найти интервалы, на которых функция убывает
# Построить график
# Вычислить вершину
# Определить промежутки, на котором f > 0
# Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt
import simpy

x_list = [i for i in range(-5,6)]
print(x_list)

def my_func(x):
    return -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

x = np.linspace(-10, 10, 5)
y = -12 * x ** 4 * np.sin(np.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30    

#направление графика
my_dif = np.diff(y)
print(my_dif)
print(f'вершина :{max(my_dif)}')

#plot простороение графика
fig, ax = plt.subplots()

ax.plot(x, y, linewidth =2.0)
# ax.plot(np.delete(x, 99), my_dif, linewidth=2.0)


coeff = [-12, -18, 5, 10]
print(f'корни уравнения: X, Y, Z :{np.roots(coeff)}')

plt.grid(True) #сетка
plt.show()