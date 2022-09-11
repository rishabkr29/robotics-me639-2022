import numpy as np
import matplotlib.pyplot as plt
import time

# Function that generates the set of points in the trajectory of the end effector
def end_effector():
    xy = []
    for i in range(20, 50): #generates 30 points
        xy.append(
            (1, i*0.05)  
        )
    
    n = len(xy)
    half_n = int(n/2)

    xy = xy[half_n:]+xy[::-1]+xy[0:half_n] # for the spring pattern, copying second half of the points first, then the reverse of entire array then the first half
    
    return xy

# Function that computes the angles q1 and q2
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
  
trajectory_points = end_effector()

# Just for plotting, converting list of pairs to list of Xs and Ys
trajectory_x_list = [x for x, y in trajectory_points]
trajectory_y_list = [y for x, y in trajectory_points]


counter = 1

# GUI Init for the matplot
plt.ion()

# creating the plot figure
figure, ax = plt.subplots(figsize=(10, 8))
arm1, = ax.plot([0,0], [0, 0]) #arm1 line
arm2, = ax.plot([0,0], [0, 0]) #arm2 line
#limits of axes of the graph
plt.xlim([0, r+0.1])
plt.ylim([0, r+0.1])

trajectory_points = trajectory_points + trajectory_points
for x, y in trajectory_points:
    q1, q2 = compute_q1_q2(x, y, l1, l2)
        
    # Plotting l1 line
    x1 = l1 * np.cos(q1)
    y1 = l1 * np.sin(q1)

    x2 = l1 * np.cos(q1) + l2 * np.cos(q2)
    y2 = l1 * np.sin(q1) + l2 * np.sin(q2)

    # Chaning values of arm1 and arm2 lines end points
    arm1.set_xdata([x0, x1])
    arm1.set_ydata([y0, y1])
    
    arm2.set_xdata([x1, x2])
    arm2.set_ydata([y1, y2])
    
    # drawing on the graph canvas and flushing it
    figure.canvas.draw()
    
    figure.canvas.flush_events()

    time.sleep(0.1) #sleep function to slow down the loop by 0.1s to visualize the animation








     