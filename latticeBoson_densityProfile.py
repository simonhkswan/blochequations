import matplotlib.pyplot as plt
import numpy as np

def N3(u):
    return(u**2)
def N2(u):
    return(u**0)
def N1(u):
    return((u-1.5)**0.5+1)

def N(u):
    return(2.5*3.1415*(u-1.5)+10*(u-1)**0.5+10*u**2*(u**0.5-(u-1)**0.5)-20/3*u*(u**1.5-(u-1)**1.5)+20*(u**2.5-(u-1)**2.5))

def profile(u,ax,col=[0,0,0]):

    R1 = 10*(u-1.5)**0.5
    R2 = 10*(u-1)**0.5
    R3 = 10*u**0.5

    q1 = np.linspace(-R1,0,4301)
    q2 = np.linspace(-R2,-R1,4301)
    q3 = np.linspace(-R3,-R2,4301)
    r1 = np.linspace(0,R1,4301)
    r2 = np.linspace(R1,R2,4301)
    r3 = np.linspace(R2,R3,4301)

    m1 = N1(u-0.01*q1**2)
    m2 = N2(u-0.01*q2**2)
    m3 = N3(u-0.01*q3**2)
    n1 = N1(u-0.01*r1**2)
    n2 = N2(u-0.01*r2**2)
    n3 = N3(u-0.01*r3**2)

    ax.plot(q1,m1,q2,m2,q3,m3,r1,n1,r2,n2,r3,n3,color=col)
fig = plt.figure(figsize = (8,6))
ax = fig.gca()
ax.set_ylabel('number density, n')
ax.set_xlabel('radius from center, r')
ax.set_title('density profiles for bosons in lattice potential')
fig.tight_layout()

n=15
m=10.0
for i in np.linspace(1.5,m,n):
    profile(i,ax,col=[i/m,1-i/m,1-i/m])

plt.savefig('densityprofiles.png',dpi=300)
#plt.show()

us = np.linspace(1.5,5,100)
totN = N(us)

fig2 = plt.figure(2,figsize=(6,8))
ax2 = fig2.gca()
ax2.set_title(r'Total particle number as a function of $\mu_0$')
ax2.set_xlabel(r'chemical potential, $\mu_0$')
ax2.set_ylabel('particle number, N')
ax2.set_xlim(1.3,5.2)
ax2.set_ylim(30,500)
ax2.plot(us,totN,color=[0.65,0.1,0.2])
ax2.plot([1,2,2],[100,100,0],'k--')

ax2.savefig('totalNmu.png',dpi=300)
#plt.show()
