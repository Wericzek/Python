import math as m
import random as r

def iloczyn_skalarny(x, y):
    z = len(x) * [0]
    for i in range(len(x)):
        z[i] = x[i] * y[i]
    return z

def wektor(leng):
    w = leng * [0]
    for i in range(leng):
        w[i] = r.randint(0,100)
    return w

x = wektor(3)
y = wektor(3)
print(" Wektory x i y: ", x, y)
print("Iloczyn: ", iloczyn_skalarny(x,y))

x1= [1,2,12,4]
y1= [2,4,8,2]
print("Iloczyn:", iloczyn_skalarny(x1, y1))