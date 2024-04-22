# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 12:16:57 2024

@author: Sven
"""

import numpy as np
import matplotlib.pyplot as plt

def damped_sinusoidal(t, A, lam, f, phi):
    return A * np.exp(-lam * t) * np.cos(2 * np.pi * f * t + phi)

# Generate time data
t = np.linspace(0, 10, 1000)  # 1000 points from 0 to 10 seconds

# Define parameters
A = 1.0  # Amplitude
lam = 0.1  # Damping factor
f = 1.0  # Frequency
phi = np.pi / 4  # Phase angle (45 degrees in radians)

# Generate data for the damped sinusoidal curve
data = damped_sinusoidal(t, A, lam, f, phi)
np.savetxt('damped_sinusoidal_data.csv', np.vstack((t, data)).T, delimiter=',',
           header='Time,Amplitude', comments='')

#%% boxplot

np.random.seed(42)
# Generate data for box plot
normal_data = np.random.normal(loc=0, scale=1, size=100)
uniform_data = np.random.uniform(low=-1, high=1, size=100)
exponential_data = np.random.exponential(scale=1, size=100)

# Combine the datasets
data = [normal_data, uniform_data, exponential_data]
headers = 'Normal,Uniform,Exponential'
np.savetxt('data_2.csv', np.vstack( data).T, delimiter=',', header=headers, comments='')

#%% 3d data

# Generate 3D data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Combine x, y, and z coordinates into a single array
data = np.column_stack((x.ravel(), y.ravel(), z.ravel()))

# Export data to CSV
np.savetxt('3d_plot_data.csv', data, delimiter=',', header='X,Y,Z', comments='')

