import numpy as np
import matplotlib.pyplot as plt


def end_effector(r, n_theta):
    # Start radius of trajectory
    theta_start=np.pi/8
    theta_end=np.pi/3

    #empty arrays for angles
    theta_list=[]

    for i in range(0, n_theta):
        tmp = theta_start + i * (theta_end - theta_start)/(n_theta-1)
        theta_list.append(tmp)
            
    xy = []
    for theta in theta_list:
        xy.append(
            (r * np.cos(theta), r * np.sin(theta))  
        )
            
    return xy

def compute_q1_q2(x, y, l1, l2):
    theta = np.arccos((x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2))
    q1 = np.arctan(y/x) - np.arctan(l2*np.sin(theta) / (l1+l2*np.cos(theta)))
    q2 = q1 + theta
    return q1, q2

def compute_torque(fx, fy, l1, l2, q1, q2):
    t1 = -fx*l1*np.sin(q1) + fy*l1*np.cos(q1)
    t2 = -fx*l2*np.sin(q2) + fy*l2*np.cos(q2)
    return t1, t2

# Fixed point of the arm
x0 = 0
y0 = 0
# Length of the arm
l1 = 2
l2 = 1  

# Constant force
fx = 10
fy = 10

# Radius of trajectory
r = 2.5

# Number of points 
n = 2
  
trajectory_points = end_effector(r, n)

# Just for plotting, converting list of pairs to list of Xs and Ys
trajectory_x_list = [x for x, y in trajectory_points]
trajectory_y_list = [y for x, y in trajectory_points]


# Initial position of arm
plt.figure()
x, y = trajectory_x_list[0], trajectory_y_list[0]
plt.scatter(x, y)
q1, q2 = compute_q1_q2(x, y, l1, l2)

## Lower arm
x1 = l1 * np.cos(q1)
y1 = l1 * np.sin(q1)
plt.plot([x0, x1], [y0, y1])

## Upper arm
x2 = l1 * np.cos(q1) + l2 * np.cos(q2)
y2 = l1 * np.sin(q1) + l2 * np.sin(q2)
plt.plot([x1, x2], [y1, y2])
plt.xlim([0, r+0.1])
plt.ylim([0, r+0.1])

plt.show()


# Final position of arm / wall
plt.figure()
x_init, y_init = trajectory_x_list[0], trajectory_y_list[0]
plt.scatter(x_init, y_init)

x, y = trajectory_x_list[1], trajectory_y_list[1]
plt.scatter(x, y)
plt.plot([0.5, x+1], [y, y])
q1, q2 = compute_q1_q2(x, y, l1, l2)

## Lower arm
x1 = l1 * np.cos(q1)
y1 = l1 * np.sin(q1)
plt.plot([x0, x1], [y0, y1])

## Upper arm
x2 = l1 * np.cos(q1) + l2 * np.cos(q2)
y2 = l1 * np.sin(q1) + l2 * np.sin(q2)
plt.plot([x1, x2], [y1, y2])
plt.xlim([0, r+0.1])
plt.ylim([0, r+0.1])

# Compting torque
t1, t2 = compute_torque(fx, fy, l1, l2, q1, q2)
plt.text(x0+0.08, y0+0.05, "t1 = "+str(round(t1, 4)) +" Nm", fontsize=10)
plt.text(x1+0.01, y1+0.05, "t2 = "+str(round(t2, 4)) +" Nm", fontsize=10)

plt.text(x2-0.5, y2+0.08, "Fx = " + str(round(fx, 4)) + " N, Fy = " + str(round(fy, 4)) + " N", fontsize=10)


plt.show()

