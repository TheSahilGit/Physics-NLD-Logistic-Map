### Logistic Map and bifurcation diagam code. ###
### Sahil Islam ###
### 23/06/2020 ###

import matplotlib.pyplot as plt
import numpy as np


def f(r, x):
    return r * x * (1 - x)


def bifurcationDiagram(xo):
    xs = []
    rs = []
    for r in np.arange(0.0, 4.0, 0.004):
        x = xo
        for i in range(200):
            x = f(r, x)
            if i > 100:
                xs.append(f(r, x))
                rs.append(r)

    col = np.linspace(100, 150, len(xs))

    plt.scatter(rs, xs, s=5, marker='.', c=col, cmap='hsv')
    plt.xlabel("$r$")
    plt.ylabel("$x$")
    plt.grid()
    plt.title("Logistic Map \n Bifurcation Diagram")
    plt.show()


def cobwebDiagram(r, xo):
    y1s = []
    y2s = []
    x = np.linspace(0, 1, 500)

    for i in x:
        y1 = f(r, i)
        y2 = i

        y1s.append(y1)
        y2s.append(y2)

    px = np.empty(100)
    py = np.empty(100)
    px[0] = xo
    py[0] = 0
    px[1] = xo
    py[1] = f(r, px[0])
    for j in range(1, len(px) - 1):
        px[j + 1] = py[j]
        py[j + 1] = f(r, px[j])

    plt.plot(x, y1s)
    plt.plot(x, y2s)
    plt.plot(px, py)
    plt.plot()
    plt.title(" Logistic Map \n Cobweb Diagram")
    plt.xlabel("$x_n$")
    plt.ylabel("$x_{n+1}$")
    plt.grid()
    plt.show()


def generationDiagram(r, xo):
    xs = []
    ns = []
    x = xo
    for i in range(200):
        x = f(r, x)

        xs.append(f(r, x))
        ns.append(i)

    print(len(ns))
    print(len(xs))
    plt.plot(ns, xs)
    plt.xlabel("$n$")
    plt.ylabel("$x$")
    plt.grid()
    plt.title("Logistic Map \n Generation Diagram")
    plt.show()


def generationMultiplotDiagram(minr, maxr, xo, maxIteration):
    def solveLoop(r):
        xs = []
        ns = []
        x = xo
        for i in range(maxIteration):
            x = f(r, x)

            xs.append(f(r, x))
            ns.append(i)

        return xs, ns

    r = minr
    interval = (maxr - minr) / 4
    for i in range(1, 5):
        xs, ns = solveLoop(r)
        plt.subplot(2, 2, i)
        plt.plot(ns, xs)
        r += interval
        plt.title("Logistic Map" "\n" "Population Vs Generation Number\n" "r=" + str(round(r, 4)))
        plt.xlabel("Generation Number(n)")
        plt.ylabel("Population Variable(x)")
        plt.subplots_adjust(0.12, 0.11, 0.90, 0.88, 0.26, 0.66)
        plt.grid()
    plt.show()


# generationMultiplotDiagram(2.5, 3.5, 0.2, 30)

# cobwebDiagram(3.99, 0.1)

# bifurcationDiagram(0.2)
