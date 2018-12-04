class zespolone:
    def __init__(self, re, im):
        self.Re = re
        self.Im = im

    def __add__(self, other):
        return zespolone(other.Re + self.Re, other.Im + self.Im)

    def __sub__(self, other):
        return zespolone(self.Re - other.Re, self.Im - other.Im)



    def __str__(self):
        return str(self.Re) + "+" + str(self.Im) + "i"
x = zespolone(1,20)
y = zespolone(9,19)
print(x + y)
