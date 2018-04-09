import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp

def c_d(q,l):
    return ((q+2*l*k)**2)/(2*m) - V/2

def c_o(q,l):
    return -V/4

def H(q):
    Hq = []
    for m in range(15):
        Hq.append([0,]*15)
    for j in range(-7,8):
        for i in range(-7,8):
            if i - j == 0:
                Hq[i+7][j+7] = c_d(q,i)
            if abs(i-j) == 1:
                Hq[i+7][j+7] = c_o(q,i)
    G = np.array(Hq)
    w,vr = sp.eig(G)

    w.sort()
    return(w[0])

def mkplot(v,axes):
    global V
    V = v
    E = []
    Q = np.linspace(-5,5,471)
    for q in Q:
        E.append(H(q).real)

    t = 0.25*(max(E)-min(E))
    axes.plot(Q,E)
    return(t)

h=1
m=1
k=3

fig1 = plt.figure(1,figsize=(4,8))
ax1 = fig1.gca()
ax1.set_title('Band Structure for various well depths')
ax1.set_xlabel('Wave vector, q')
ax1.set_ylabel('Energy, E')
fig2 = plt.figure(2,figsize=(8,5))
ax2 = fig2.gca()
ax2.set_title('Tunnelling Constant as a funciton of well depth')
ax2.set_xlabel('Tunnelling constant, t')
ax2.set_ylabel('Well depth, V0')

Vs = [0,0.1,1,2,5,10]
t = []

for V0 in Vs:
    t.append(mkplot(V0,ax1))
ax2.plot(Vs,t,'x')

fig1.savefig('bandstructure.png', dpi=300)
fig2.savefig('tunnelling.png', dpi=300)
