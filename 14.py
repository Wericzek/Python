import random as r
size = 3
print("Macierz wygenerowana losowo o rozmiarze : ", size, "x" , size)
#size = 3
wiersz = {}
for i in range(size):
    wiersz[i] = []
    for _ in range(size):
        wiersz[i].append(r.randint(0,10))
    print(str(wiersz[i]))

print("Wyznacznik wynosi : ")
a = wiersz[0][0] * wiersz[1][1] + wiersz[1][0] * wiersz[0][1]
print(a)