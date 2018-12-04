with open ('plik.txt', 'r') as wejscie:
	with open ('zapis.txt', 'w') as wyjscie:
		for line in wejscie:
			wyjscie.write(" wez z plik.txt: " + line)
print("OK")