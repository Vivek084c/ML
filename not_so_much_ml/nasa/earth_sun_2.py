import numpy as np
import plotly.graph_objects as go

# Orbital parameters for Earth's orbit around the Sun
a = 1.496e11  # Semi-major axis in meters (1 AU)
e = 0.0167    # Eccentricity
i = np.radians(0.00005)  # Inclination in radians (almost 0 for Earth's orbit)
Omega = np.radians(-11.26064)  # Longitude of ascending node in radians
omega = np.radians(114.20783)  # Argument of perihelion in radians
T = 365.25 * 24 * 3600  # Orbital period in seconds (1 year)

# Kepler's Equation: Solve for Eccentric Anomaly (E) using Newton-Raphson method
def solve_keplers_equation(M, e, tol=1e-6):
    E = M if e < 0.8 else np.pi  # Initial guess for E
    while True:
        delta_E = (M - E + e * np.sin(E)) / (1 - e * np.cos(E))
        E = E + delta_E
        if np.abs(delta_E) < tol:
            break
    return E

# True Anomaly (nu) from Eccentric Anomaly (E)
def true_anomaly(E, e):
    return 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2), np.sqrt(1 - e) * np.cos(E / 2))

# 3D position in the orbital plane (x', y')
def get_orbital_position(a, e, nu):
    r = a * (1 - e**2) / (1 + e * np.cos(nu))  # Distance from Sun
    x_prime = r * np.cos(nu)
    y_prime = r * np.sin(nu)
    return x_prime, y_prime, r

# Rotate the 2D orbital plane coordinates to 3D using the orbital elements
def rotate_to_3d(x_prime, y_prime, Omega, i, omega):
    x = (np.cos(Omega) * np.cos(omega) - np.sin(Omega) * np.sin(omega) * np.cos(i)) * x_prime + \
        (-np.cos(Omega) * np.sin(omega) - np.sin(Omega) * np.cos(omega) * np.cos(i)) * y_prime
    y = (np.sin(Omega) * np.cos(omega) + np.cos(Omega) * np.sin(omega) * np.cos(i)) * x_prime + \
        (-np.sin(Omega) * np.sin(omega) + np.cos(Omega) * np.cos(omega) * np.cos(i)) * y_prime
    z = (np.sin(omega) * np.sin(i)) * x_prime + (np.cos(omega) * np.sin(i)) * y_prime
    return x, y, z

# Simulate Earth's orbit around the Sun
def simulate_orbit(a, e, i, Omega, omega, T, steps=1000):
    positions = []
    for t in np.linspace(0, T, steps):
        M = 2 * np.pi * (t / T)  # Mean anomaly
        E = solve_keplers_equation(M, e)  # Eccentric anomaly
        nu = true_anomaly(E, e)  # True anomaly
        x_prime, y_prime, r = get_orbital_position(a, e, nu)  # Orbital plane position
        x, y, z = rotate_to_3d(x_prime, y_prime, Omega, i, omega)  # Convert to 3D position
        positions.append([x, y, z])
    return np.array(positions)

# Run the simulation
positions = simulate_orbit(a, e, i, Omega, omega, T)

# Create an interactive 3D plot using Plotly
fig = go.Figure()

# Plot the Earth's orbit
fig.add_trace(go.Scatter3d(
    x=positions[:, 0],
    y=positions[:, 1],
    z=positions[:, 2],
    mode='lines',
    line=dict(color='blue', width=2),
    name='Earth Orbit'
))

# Plot the Sun at the origin
fig.add_trace(go.Scatter3d(
    x=[0],
    y=[0],
    z=[0],
    mode='markers',
    marker=dict(color='yellow', size=10),
    name='Sun'
))

# Customize the layout
fig.update_layout(
    title="Earth's Orbit Around the Sun",
    scene=dict(
        xaxis_title='X (meters)',
        yaxis_title='Y (meters)',
        zaxis_title='Z (meters)',
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Show the interactive plot
fig.show()