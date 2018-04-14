import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as sp

def c_d(q,l):
    return((h**2*(q+2*l*k)**2)/(2*m) - V/2)

def c_o(q,l):
    return(-V/4)

def H(q):
    Hq = []
    for m in range(15):
        Hq.append([0,]*15)
    for j in range(-7,8):
        for i in range(-7,8):
            if i - j == 0:
                Hq[i+7][j+7] = c_d(q,i)/Er
            if abs(i-j) == 1:
                Hq[i+7][j+7] = c_o(q,i)/Er
    G = np.array(Hq)
    w,vr = sp.eig(G)

    w.sort()
    return(w[0])

def mkplot(v,axes):
    global V
    V = v
    E = []
    Q = np.linspace(-1.7*k,1.7*k,471)
    for q in Q:
        E.append(H(q).real)

    t = 0.25*(max(E)-min(E))*Er/h*pi*2
    axes.plot(Q,E-min(E))
    return(t)

def U(V):
    return(((2*a*((2*h*m/pi)**0.5)*((4*V*(k**2)/m)**0.75))/h))

def W(V):
    return((4*V*k**2/m)**0.5)/pi/2


h = 1.055*10**-34
pi = 3.14159
m = 87*1.67*10**-27
k = 2*pi/(830*10**(-9))
a = 100*0.5*10**-10
Er = 3.663*10**-30

fig1 = plt.figure(1,figsize=(4,8))
ax1 = fig1.gca()
ax1.set_title('Band Structure for various well depths')
ax1.set_xlabel('Wave vector, q')
ax1.set_ylabel('Energy, E')
fig2 = plt.figure(figsize=(4,8))
ax2 = fig2.gca()
ax2.set_title('Tunnelling Constant as a funciton of well depth')
ax2.set_ylabel('w,t,U / Hz')
ax2.set_xlabel('Well depth, V0')
ax2.set_ylim(0,80000)
fig3 = plt.figure(3)
ax3 = fig3.gca()
ax3.set_title('Ratio of U/t as a function of well depth')
ax3.set_ylabel('U/t')
ax3.set_xlabel('Well depth, V0')
ax3.set_ylim(0,1000)

Vs = np.linspace(0,30*Er,60)
t = []
Ut = []

for V0 in Vs:
    tunnel = mkplot(V0,ax1)
    t.append(tunnel)
    Ut.append(U(V0)/tunnel)

ax2.plot(Vs/Er,t,'b')
ax3.plot(Vs/Er,Ut,'x-')
ax2.plot(Vs/Er,U(Vs),'r')
ax2.plot(Vs/Er,W(Vs),'k')
fig2.tight_layout()
#plt.show()

fig1.savefig('bandstructure.png', dpi=300)
fig2.savefig('tUw_sizes.png', dpi=300)
fig3.savefig('UtRatio.png', dpi=300)
