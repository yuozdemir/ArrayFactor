import numpy as np
import matplotlib.pyplot as plt


def gain(d, w, n):
    print(d, w, n)
    phi = np.linspace(0, 2 * np.pi, 1000)
    psi = (2 * np.pi) * (d / lam) * (np.cos(phi) + beta)
    A = 0
    for i in range(n):
        A = A + w[i] * np.exp(1j * psi * i)
    g = np.abs(A) ** 2
    print(g)
    return phi, g


def get_directive_gain(g, minDdBi):
    DdBi = 10 * np.log10(g / np.max(g))
    return np.clip(DdBi, minDdBi, None)


N = [2, 4, 6, 8, 10, 12]
beta = 90
lam = 1
d = lam / 2
minDdBi = -60
w = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

lw = 2
ls = ['-', '--', '-.', '-', ':', '-', '--', '-.', '-', ':', '-']

phi_pi = np.linspace(0, 2 * np.pi, 1000)
phi_180 = []
for i in range(len(phi_pi)):
    phi_180.append(phi_pi[i] * (180 / np.pi))

########################################################################################################################
for i in range(len(N)):
    phi, g = gain(d, w, N[i])
    DdBi = get_directive_gain(g, minDdBi)

    plt.plot(phi_180, DdBi, linewidth=lw, linestyle=ls[i])
    plt.legend(N, title='N Number')

font1 = {'family': 'serif', 'color': 'black', 'size': 15}

plt.title("AF", fontdict=font1)
plt.xlabel("Theta (degree)")
plt.ylabel("Array Factor (dB)")

plt.axis([0, 180, -60, 0])

plt.grid(axis='y', color='black', linestyle='--', linewidth=0.1)
########################################################################################################################

plt.figure()

########################################################################################################################
for i in range(len(N)):
    phi, g = gain(d, w, N[i])
    DdBi = get_directive_gain(g, -20)

    plt.polar(phi, DdBi, linewidth=lw, linestyle=ls[i])

    plt.legend(N, title='N Number')

ax = plt.gca()
ax.set_rticks([-20, -15, -10, -5])
ax.set_rlabel_position(45)
########################################################################################################################

plt.show()
