import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
epsilon = np.radians(23.43928)  # Earth's axial tilt (in radians)
AU = 1.496e+11  # Astronomical Unit in meters (for scaling)
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30  # Mass of the Sun (kg)

# Keplerian elements for Earth (example values)
a = 1.00000261  # Semi-major axis (AU)
e = 0.01671123  # Eccentricity
I = np.radians(0.00005)  # Inclination (radians)
L = np.radians(100.46457166)  # Mean longitude (radians)
omega_bar = np.radians(102.93768193)  # Longitude of perihelion (radians)
Omega = np.radians(0)  # Longitude of the ascending node (radians)

# Kepler's equation solver to find eccentric anomaly (E)
def solve_kepler(M, e, tol=1e-6):
    E = M if e < 0.8 else np.pi
    delta_E = 1
    while abs(delta_E) > tol:
        delta_E = (M - (E - e * np.sin(E))) / (1 - e * np.cos(E))
        E += delta_E
    return E

# Rotation matrices to convert to the ecliptic plane
def rotate_z(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                     [np.sin(angle), np.cos(angle), 0],
                     [0, 0, 1]])

def rotate_x(angle):
    return np.array([[1, 0, 0],
                     [0, np.cos(angle), -np.sin(angle)],
                     [0, np.sin(angle), np.cos(angle)]])

# Function to compute the position of the planet
def compute_position(T):
    # Mean anomaly
    M = L + (2 * np.pi / 365.25) * T - omega_bar
    E = solve_kepler(M, e)

    # Orbital coordinates
    x_prime = a * (np.cos(E) - e)
    y_prime = a * np.sqrt(1 - e**2) * np.sin(E)
    z_prime = 0

    # Rotation to ecliptic plane
    r_prime = np.array([x_prime, y_prime, z_prime])
    rotation_matrix = rotate_z(-Omega) @ rotate_x(-I) @ rotate_z(-omega_bar)
    r_ecliptic = rotation_matrix @ r_prime

    # Convert to equatorial coordinates
    x_ecl, y_ecl, z_ecl = r_ecliptic
    x_eq = x_ecl
    y_eq = y_ecl * np.cos(epsilon) - z_ecl * np.sin(epsilon)
    z_eq = y_ecl * np.sin(epsilon) + z_ecl * np.cos(epsilon)

    # Scale to astronomical units (optional)
    return x_eq * AU, y_eq * AU, z_eq * AU

# Function to calculate the angular velocity
def angular_velocity(pos1, pos2, dt):
    r1 = np.linalg.norm(pos1)
    r2 = np.linalg.norm(pos2)
    delta_theta = np.arccos(np.dot(pos1, pos2) / (r1 * r2))  # angle between the two positions
    return delta_theta / dt

# Set up the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Time variables (number of days to simulate)
num_days = 365
positions = []
angular_velocities = []
time_steps = []

# Simulate Earth's motion for one year
for T in range(num_days):
    pos = compute_position(T)
    positions.append(pos)
    
    # Compute angular velocity for current and previous positions
    if T > 0:
        angular_vel = angular_velocity(np.array(positions[T-1]), np.array(pos), 1)
        angular_velocities.append(angular_vel)
        time_steps.append(T)

# Convert positions to arrays for easier plotting
positions = np.array(positions)
x_vals = positions[:, 0]
y_vals = positions[:, 1]
z_vals = positions[:, 2]

# Plot Earth's orbit around the Sun
ax.plot(x_vals, y_vals, z_vals, label="Earth's Orbit")

# Plot the Sun at the origin
ax.scatter(0, 0, 0, color='yellow', s=300, label='Sun')

# Add labels and title
ax.set_xlabel('X (meters)')
ax.set_ylabel('Y (meters)')
ax.set_zlabel('Z (meters)')
ax.set_title("Earth's Orbit Around the Sun")

# Scale axis
ax.auto_scale_xyz([-AU, AU], [-AU, AU], [-AU, AU])

# Show the 3D orbit plot
plt.legend()
plt.show()

# Plot angular velocity over time
plt.figure()
plt.plot(time_steps, angular_velocities, label='Angular Velocity', color='green')
plt.xlabel('Time (days)')
plt.ylabel('Angular Velocity (rad/day)')
plt.title('Angular Velocity of Earth Around the Sun')
plt.legend()
plt.grid(True)
plt.show()