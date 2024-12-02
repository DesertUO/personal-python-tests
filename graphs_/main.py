import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

t = np.arange(0., 5., 0.01)

def main():
    # Red dashes, blue squares and green triangles
    # plt.plot(t, t, "r--", t, np.cos(pi*t), "bs", t, np.sin(pi*t), "g^")


    def f(t):
        return np.exp(-t) * np.cos(2*pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure()
    plt.subplot(211)
    plt.title("Plot 1")
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.grid(True)

    plt.subplot(212)
    plt.title("Plot 2")
    plt.plot(t2, np.cos(2*pi*t2), 'r--')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
