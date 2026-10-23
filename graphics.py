#добавляем нужные нам библиотеки
import matplotlib.pyplot as plt
import numpy as np
#зададим область определения для функций
x = range(-50, 51) 
#зададим квадратичную функцию
y = [i**2 for i in x]
#зададим показательную функцию
b = np.exp(x)
#зададим логарифмическую функцию
m = np.log(x)
#зададим кубическую функцию 
l = [z**3 for z in x]
#напишем команду для вывода нескольких графиков сразу
fig, f = plt.subplots(1, 4, figsize=(67, 52))
f[0].grid(True)#команда для создания сетки для графика выбранного окна 
f[0].plot(x, y, "X-", color="brown", markersize=8) #команда, отрисовывающая график с заданным дизайном 
f[1].grid(True)
f[1].plot(x, b, "o-", color="purple", markersize=8)
f[2].grid(True)
f[2].plot(x, m, "^-", color="pink", markersize=8)
f[3].grid(True)
f[3].plot(x, l, "*-", color="orange", markersize=8)
#команда для вывода графиков
plt.show()
