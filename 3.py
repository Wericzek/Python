import os
directory = '/dev'
lista = os.listdir(directory)
#fil = len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
print("Liczba plikow znajdujacych sie w katalogu /dev")
print(len(lista))
#print(fil)