import numpy as np
import matplotlib.pyplot as plt
import time


def end_effector(r, n_theta):
    # Start radius of trajectory
    theta_start=np.pi/8
    theta_end=np.pi/2

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

# Fixed point of the arm
x0 = 0
y0 = 0
# Length of the arm
l1 = 2
l2 = 1  

# Radius of trajectory
r = 2.5

# Number of points 
n = 200
  
trajectory_points = end_effector(r, n)

plt.ion()

figure, ax = plt.subplots(figsize=(10, 8))
arm1, = ax.plot([0,0], [0, 0])
arm2, = ax.plot([0,0], [0, 0])
#scatter, = ax.scatter([], [])
plt.xlim([0, r+0.1])
plt.ylim([0, r+0.1])

#plt.show()
    

# Just for plotting, converting list of pairs to list of Xs and Ys
trajectory_x_list = [x for x, y in trajectory_points]
trajectory_y_list = [y for x, y in trajectory_points]

# plotting end effector point
plt.scatter(trajectory_x_list, trajectory_y_list)

counter = 1
for x, y in trajectory_points:
    q1, q2 = compute_q1_q2(x, y, l1, l2)
    

    
    # Plotting l1 line
    x1 = l1 * np.cos(q1)
    y1 = l1 * np.sin(q1)
    
    # plt.plot([x0, x1], [y0, y1])
    arm1.set_xdata([x0, x1])
    arm1.set_ydata([y0, y1])
    
    arm2.set_xdata([x0, x1])
    arm2.set_ydata([y0, y1])
    

    
    # Plotting l2 line
    x2 = l1 * np.cos(q1) + l2 * np.cos(q2)
    y2 = l1 * np.sin(q1) + l2 * np.sin(q2)
    
    arm2.set_xdata([x1, x2])
    arm2.set_ydata([y1, y2])
    #plt.plot([x1, x2], [y1, y2])
    
    figure.canvas.draw()
    
    figure.canvas.flush_events()

    # time.sleep(0.01)
   
    #plt.savefig(filename)
    

    
    





     