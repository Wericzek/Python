import random as r

size = 128
macierz1 = []
macierz2 = []
msuma = []

for i in range(0, size):
	macierz1.append([])
	macierz2.append([])
	for j in range(0, size):
		macierz1[i].append(int(round(r.random()*100)))
		macierz2[i].append(int(round(r.random()*100)))

for i in range(0, size):
	msuma.append([])
	for j in range(0, size):
		msuma[i].append(macierz1[i][j] + macierz2[i][j])
print(macierz1)
print(macierz2)
print(msuma)