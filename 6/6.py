import os

directory = '/Users/plweopy/Desktop/python/6'
lista = os.listdir(directory)
print(lista)
print("Program dokona zamiany rozszerzeń plikow jpg na png")

def change_ext(old_ext, new_ext):
    files = os.listdir(directory)
    for filename in files:
        file_ext = os.path.splitext(filename)[1]
        if old_ext == file_ext:
            newfile = filename.replace(old_ext, new_ext)
            os.rename(filename, newfile)


old = '.jpg'
new = '.png'
change_ext(old, new)
lista = os.listdir(directory)
print(lista)
