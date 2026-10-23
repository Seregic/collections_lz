import numpy as np 
N = int(input("Введите количество строк : "))
M = int(input("Введите количество столбцов : "))
a = np.random.randint(0,1000,size = (N,M))
print(a)
b = np.transpose(a)
print(b)
c = np.linalg.det(a)
d = np.linalg.det(b)
if (d > c):
    print(d,">",c," Определитель d больше определителя c")
elif (d < c) : 
    print(d,"<",c," Определитель d меньше опредетителя c")
elif (np.isclose(d,c)) :
    print(d,"=",c," Определители d и c равны")
