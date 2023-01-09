#!/usr/bin/env python
# coding: utf-8

# In[65]:


import time
import os
import csv
import pandas as pd
import numpy as np

red = "\u001b[41m"
white = "\u001b[47m"
blue = "\u001b[44m"
black = "\u001b[40m"
reset = "\u001b[0m"

print(white +"\x20" * 3 + blue + "\x20" * 2 + white +"\x20" * 8 + reset)
print(blue +"\x20" * 3 + blue + "\x20" * 2 + blue +"\x20" * 8 + reset)
print(white +"\x20" * 3 + blue + "\x20" * 2 + white +"\x20" * 8 + reset)
print()

r = 7 #радиус
circles = 10 #количество повторений
mapa = [['.' for x in range(r*2+1)] for y in range(r*2+1)] #Вместо символов можно юзать цвета mapa = [[colour.white for x in range(r*2+1)] for y in range(r*2+1)]

for y in range(r*2+1):
    for x in range(r*2+1):
        if abs((x-r)**2-1 + (y-r)**2-1) < r**2:
            mapa[y][x] = '#' #Вместо символов можно юзать цвета mapa[y][x] = colour.black , но так красивее

mapa2 = mapa
for line in range(len(mapa2)):
    print(" ".join(mapa2[line])*circles) # В юпитере все поехало, в google colab прекрасная картинка
    
n = 50
coord = [["\x20" for j in range(n)] for i in range(n)]

for i in range(n):
    coord[n-1][i] = "-"
    coord[i][0] = "|"
y = n
for x in range(int(n)):
    y -= 2
    if y < n and y < 0:
        coord[x][y] = "*"

coord[n-1][n - 1] = ">"
coord[0][0] = "^"

for i in range(n):
    print("".join(e for e in coord[i]))
    
print()

a = []

with open('books.csv','r') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    for row in table:
        a.append(row)
        
col = a[0]
a = a[1:len(a)]
a = pd.DataFrame(a, columns = col)

a = a.astype({'Цена поступления': np.float})
bol200 = a.loc[(a['Цена поступления'] > 200)]
meni200 = a.loc[(a['Цена поступления'] <= 200)]

print()
print("больше 200:", blue + "\x20" * round(len(bol200)/(len(bol200)+len(meni200))*100) + reset + str(round(len(bol200)/(len(bol200)+len(meni200))*100))+"%")
print("до 200    :", blue + "\x20" * round(len(meni200)/(len(bol200)+len(meni200))*100) + reset + str(round(len(meni200)/(len(bol200)+len(meni200))*100)) + "%")


# In[ ]:




