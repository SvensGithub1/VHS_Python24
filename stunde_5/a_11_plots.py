# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:21:57 2024

@author: Sven
"""
import numpy as np
import matplotlib.pyplot as plt

# Load the data from the CSV file
data = np.loadtxt('damped_sinusoidal_data.csv', delimiter=',', skiprows=1)

# Extract time and amplitude data
t = data[:, 0]
amplitude = data[:, 1]

# Plot the data
# TODO

#%% 2 data
data = np.genfromtxt('data_2.csv', delimiter=',', skip_header=1)

# Separate the data into individual arrays
a = data[:, 0]
b = data[:, 1]
c = data[:, 2]

# Plot the data
# TODO

#%% 3d data

# Load the data from the CSV file
data = np.genfromtxt('3d_plot_data.csv', delimiter=',', skip_header=1)

# Separate the data into x, y, and z coordinates
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]


# Reshape the data into 2D arrays for plotting
x = x.reshape((100, 100))
y = y.reshape((100, 100))
z = z.reshape((100, 100))

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Plot the data in other ways
# TODO