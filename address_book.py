import pandas as pd
import numpy as np
a = pd.DataFrame({"ФИО : " : ["Чебупель Карлик Асталопович","Гринвич Джейк Сиксевенович"], "Адрес : " : ["Ул. Пушкина, д. Колотушкина","ул. Черная, д. 1"], "Телефон: " : ["007675242","40452426967"], "Дата рождения: " : ["67.52.2026","69.42.2000"]})
print(a)
for i in range(len(a)) :
    for j in range(len(a.columns)):
       d = int(input("Удалить - 0, Добавить - 1, Изменить  - 2 : "))
       match d: 
         case 0:
           a.iloc[i,j] = np.nan
           print(a)
         case 1:
           h = int(input("Напишите, что бы вы хотели добавить: строку(1) или столбец(2)? : "))
           match h:
              case 1:
                 fio = input("Введите ФИО : ")
                 adr = input("Введите адрес : ")
                 tel = input("Введите телефон : ")
                 dat = input("Введите дату рождения : ")
                 a.loc[len(a)] = [fio, adr, tel, dat]
              case 2: 
                  st = input("Введите название столбца : ")
                  d = []
                  for h in range(len(a)) :
                     d.append(input(f"Введите значение для {h} столбца : "))
                  a[st] = d
           print(a)
         case 2:
           f = input("Напишите , на что хотите заменить : ")
           a.iloc[i,j] = f
           print(a)

print(a)
