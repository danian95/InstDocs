#! /bin/python3

# import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Set some theoretical values of van Deemter equation
# Taken from the Wikipedia article of the 
# van Deemter Equation
# Original file by user Pronchik
A = 1.5
B = 25
C = 0.025

# Plot up to 100 on the x-axis
u = np.arange(1,100,1)

# Add the plots
plt.plot(u, A + B/u + C*u, '-', label = 'A + B/μ + Cμ')
plt.plot(u, A + 0*u, '--', label = 'A')
plt.plot(u, B/u, '--', label = 'B/μ')
plt.plot(u, C*u, '--', label = 'Cμ')
plt.legend()
plt.xlabel("Flow Rate (mL/min)")
plt.ylabel("Plate Height (mm)")

# Set the viewport
plt.axis((0,100,0,6))

plt.show()
