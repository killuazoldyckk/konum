import math
import numpy as np
import matplotlib.pyplot as plt

print("BISECTION METHOD WITH PYTHON")

a = float(input("masukkan batas atas (x1) :"))
b = float(input("masukkan batas bawah (x2) :"))
e = float(input("masukkan nilai toleransi (e) :"))
N = 100


def f(x):
    return (math.tan(x)-x-1)


def bisect(func, a, b, e, N):
    if func(a) * func(b) > 0:
        print("nilai f(a) dan f(b) harus berbeda tanda")
        
    print("i              x1            x2               xr            f(x1)          f(x2)           f(xr)")

    lastFuncVal = func(a)
    for i in range(0, N):
        c = (a+b)/2
        print(i+1, "\t", format(a, ".7f"), "\t", format(b, ".7f"), "\t", format(c, ".7f"), "\t", format(
            func(a), ".7f"), "\t", format(func(b), ".7f"), "\t", format(func(c), ".7f"))

        if func(c) == 0 or abs(f(a)*f(b)) < e:
            return c

        if func(c)*func(a) > 0:
            a = c
        else:
            b = c
        lastFuncVal = func(c)

print("Bisection method soln: x = ", bisect(f, a, b, e, N))

x = np.linspace(-10, 10, 100)
y = list(map(f, x))
plt.plot(x, y)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph of tan(x) - x - 1')
plt.grid(True)
plt.show()
