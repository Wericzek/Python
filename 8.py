import random

def randg(rang, length):
    return random.sample(range(rang), length)

print("Funkcja sortuje losowe liczby malejaca")
def sort(x):
    for i in range(50):
        for l in range(49):
            if x[l] < x[l + 1]:
                tmp = x[l]
                x[l] = x[l + 1]
                x[l + 1] = tmp
    return (x)


x = randg(1000, 50)
y = sort(x)
print(y)