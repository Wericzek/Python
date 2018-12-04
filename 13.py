import random as r


size = 8
wiersze = {}
print("Macierz 1")
for i in range(size):
    wiersze[i] = []
    for _ in range(size):
        wiersze[i].append(r.randint(0,10))
    print(str(wiersze[i]))

print("Macierz 2")
kolumny = {}
for i in range(size):
    kolumny[i] = []
    for _ in range(size):
        kolumny[i].append(r.randint(0,10))
    print(str(kolumny[i]))


print("Wynik ")
wiersze3 = {}
for i in range(size):
    wiersze3[i] = []
    for j in range(size):
        wiersze3[i].append(kolumny[i][j] + wiersze[i][j])
    print(str(wiersze3[i]))