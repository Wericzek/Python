
kod = input("Podaj szyfr zamka: ")
access = False
while access == False:
    unlock = input("Podaj szyfr: ")
    if unlock == kod:
        access = True
        print("szyfr wpisany poprawnie. Zamek otwarty")
    else:
        print("bledny szyfr")