import math as m

def f_kwadratowa(a,b,c):
    delta = b*b - 4*a*c
    if delta > 0:
        x1 = (-b-m.sqrt(delta))/2*a
        x2 = (-b+m.sqrt(delta))/2*a
        print("Rownanie kwadratowe ma dwa pierwiastki równe:", x1, x2)
    elif delta == 0:
        x1 = (-b)/2*a
        print("Rownanie kwadratowe ma jeden podwojny pierwiastek :", x1)

    elif delta <0:

        print("Rownanie nie ma rzeczywistych pierwiastkow")

a, b, c = input("Podaj wspolczynniki funkcji kwadratowej: ").split()
f_kwadratowa(int(a), int(b), int(c))
