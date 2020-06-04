### Logistic Map and bifurcation diagram code. ###
### Sahil Islam ###
### 03/04/2020 ###

import numpy as np
import matplotlib.pyplot as plt
import csv
import math


def map_function(r, x):
    return r * x * (1 - x)


def solve_loop(r, x):
    file = open("bifurcation.txt", "w+")
    for i in range(20):
        x = map_function(r, x)
        csv.writer(file).writerow([i, x, r])
    file.close()


def plot_loop1():
    data = np.loadtxt("bifurcation.txt", delimiter=',')
    ts = data[:, 0]
    xs = data[:, 1]
    rs = data[:, 2]

    plt.plot(rs, xs, '.', color='b')
    plt.title("Logistic Map" "\n" "Bifurcation Diagram")
    plt.xlabel("Growth Parameter(r)")
    plt.ylabel("Population Variable(x)")
    plt.grid()


def plot_loop2(r):
    data = np.loadtxt("bifurcation.txt", delimiter=',')
    ts = data[:, 0]
    xs = data[:, 1]
    rs = data[:, 2]

    plt.plot(ts, xs, color='blue')
    plt.title("Logistic Map" "\n" "Population Vs Generation Number\n" "r=" + str(r))
    plt.xlabel("Generation Number")
    plt.ylabel("Population Variable(x)")
    plt.grid()


def bifurcation_loop(x0):
    file = open("bifurcation.txt", "w+")
    for r in np.arange(0.0, 4.0, 0.004):
        x = x0
        for i in range(200):
            x = r * x * (1 - x)
            if i > 100:
                csv.writer(file).writerow([i, x, r])
    file.close()
    plot_loop1()


def generation_loop(r):
    solve_loop(r, 0.75)
    plot_loop2(r)


def generation_subplot_loop(r_min, r_max, x_init):
    n = 0
    interval = (r_max - r_min) / 4.0
    for r in np.arange(r_min, r_max, interval):
        n = n + 1
        solve_loop(r, x_init)
        data = np.loadtxt("bifurcation.txt", delimiter=',')
        ts = data[:, 0]
        xs = data[:, 1]
        rs = data[:, 2]
        plt.subplot(2, 2, n)
        plt.plot(ts, xs, color='blue')
        plt.title("Logistic Map" "\n" "Population Vs Generation Number\n" "r=" + str(r))
        plt.xlabel("Generation Number")
        plt.ylabel("Population Variable(x)")
        plt.subplots_adjust(0.12, 0.11, 0.90, 0.88, 0.26, 0.66)
        plt.grid()


#generation_subplot_loop(0.1, 4.0, 0.75)
#generation_loop(3.5)
#bifurcation_loop(0.75)
plt.show()
