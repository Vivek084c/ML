import numpy as np
import math

# Constants
epsilon = np.radians(23.43928)  # Earth's axial tilt (in radians)

# Keplerian elements for Earth (example values)
a = 1.00000261  # Semi-major axis (AU)
e = 0.01671123  # Eccentricity
I = np.radians(0.00005)  # Inclination (radians)
L = np.radians(100.46457166)  # Mean longitude (radians)
omega_bar = np.radians(102.93768193)  # Longitude of perihelion (radians)
Omega = np.radians(0)  # Longitude of the ascending node (radians)

# Julian century from J2000.0 (T = (Teph - 2451545.0) / 36525)
# For example, Teph = 2459396.5 is Jan 1, 2021
Teph = 2459396.5
T = (Teph - 2451545.0) / 36525.0

# Calculate the mean anomaly (M)
M = L - omega_bar

# Kepler's equation solver to find eccentric anomaly (E)
def solve_kepler(M, e, tol=1e-6):
    E = M if e < 0.8 else np.pi
    delta_E = 1
    while abs(delta_E) > tol:
        delta_E = (M - (E - e * np.sin(E))) / (1 - e * np.cos(E))
        E += delta_E
    return E

# Solve for eccentric anomaly
E = solve_kepler(M, e)

# Heliocentric coordinates in the orbital plane (r')
x_prime = a * (np.cos(E) - e)
y_prime = a * np.sqrt(1 - e**2) * np.sin(E)
z_prime = 0  # Since we are in the 2D orbital plane

# Rotation matrices to convert to the ecliptic plane
def rotate_z(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                     [np.sin(angle), np.cos(angle), 0],
                     [0, 0, 1]])

def rotate_x(angle):
    return np.array([[1, 0, 0],
                     [0, np.cos(angle), -np.sin(angle)],
                     [0, np.sin(angle), np.cos(angle)]])

# Compute the position in the J2000 ecliptic plane
r_prime = np.array([x_prime, y_prime, z_prime])
rotation_matrix = rotate_z(-Omega) @ rotate_x(-I) @ rotate_z(-omega_bar)
r_ecliptic = rotation_matrix @ r_prime

# Convert to equatorial coordinates
x_ecl, y_ecl, z_ecl = r_ecliptic
x_eq = x_ecl
y_eq = y_ecl * np.cos(epsilon) - z_ecl * np.sin(epsilon)
z_eq = y_ecl * np.sin(epsilon) + z_ecl * np.cos(epsilon)

# Output heliocentric and equatorial coordinates
print(f"Heliocentric coordinates (ecliptic plane): x = {x_ecl}, y = {y_ecl}, z = {z_ecl}")
print(f"Equatorial coordinates: x = {x_eq}, y = {y_eq}, z = {z_eq}")