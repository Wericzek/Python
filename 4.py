


code = input("Podaj szyfr zamka: ")
access = False
while access == False:
    unlock = input("Podaj szyfr: ")
    if unlock == code:
        access = True
        print("szyfr wpisany poprawnie. Zamek otwarty")
    else:
        print("bledny szyfr")