import matplotlib.pyplot as plt
import numpy as np
d2r = np.deg2rad
theta11 = np.linspace(d2r(35),d2r(145))
theta22 = np.linspace(d2r(35), d2r(145))
theta1, theta2 = np.meshgrid(theta11, theta22)

px1 = {}
py1 = {}

l1 = 2
l2 = 1

px = l1*np.cos(theta1) + l2*np.cos(theta1 + theta2)
py = l1*np.sin(theta1) + l2*np.sin(theta1 + theta2)
plt.figure()
plt.scatter(px, py)
plt.show()

