import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

h=1
m=1
V=2
k=1

def c_d(q,l):
    return ((q+2*l*k)**2)/(2*m) - V/2

def c_o(q,l):
    return -V/4

Hq = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
q = 2
for j in range(-4,5):
    for i in range(-4,5):
        g = i + 4
        n = j + 4
        if i - j == 0:
            Hq[n][g] = c_d(q,i)
        if abs(i-j) == 1:
            Hq[n][g] = c_o(q,i)

H = np.array(Hq)
print(H)
