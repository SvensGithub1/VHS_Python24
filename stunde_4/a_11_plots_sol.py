# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:21:57 2024

@author: Sven
"""
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = np.loadtxt('damped_sinusoidal_data.csv', delimiter=',', skiprows=1)

fig, ax1 = plt.subplots()
# Extract time and amplitude data
t = data[:, 0]
amplitude = data[:, 1]

# Plot the data
plt.plot(t, amplitude, linewidth=3, color='b')
plt.title('Damped Sinusoidal Curve')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
ax1.set(xlim=(-1, 12), ylim=(-2, 2))



plt.show()

#%% 2 data
data = np.genfromtxt('data_2.csv', delimiter=',', skip_header=1)

# Separate the data into individual arrays
normal_data = data[:, 0]
uniform_data = data[:, 1]
exponential_data = data[:, 2]

data = [normal_data, uniform_data, exponential_data]
labels = ['Normal', 'Uniform', 'Exponential']

# Create a figure with two subplots (box plot and histograms)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Box plot
ax1.boxplot(data, labels=labels)
ax1.set_title('Box Plot of Different Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Values')

# Histograms
ax2.hist(data, bins=20, label=labels)
ax2.set_title('Histograms of Different Distributions')
ax2.set_xlabel('Values')
ax2.set_ylabel('Frequency')
ax2.legend()

# Show the plot
plt.tight_layout()
plt.show()

# alternative

fig, ax1 = plt.subplots()
ax1.violinplot(data)
ax1.set_title('Plot of Different Distributions')
ax1.set_xlabel('Distribution')
ax1.set_ylabel('Values')

# Show the plot
plt.tight_layout()
plt.show()
#%% 3d data

# Load the data from the CSV file
data = np.genfromtxt('3d_plot_data.csv', delimiter=',', skip_header=1)

# Separate the data into x, y, and z coordinates
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

x1 = data[:, 0]
y1 = data[:, 1]
z1 = data[:, 2]

# Reshape the data into 2D arrays for plotting
x = x.reshape((100, 100))
y = y.reshape((100, 100))
z = z.reshape((100, 100))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot')

# Show the plot
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.pcolormesh(x,y,z)
# Show the plot
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.contour(x,y,z)
# Show the plot
plt.show()

fig = plt.figure()
ax = fig.add_subplot()
ax.contour(y,z,x)
# Show the plot
plt.show()