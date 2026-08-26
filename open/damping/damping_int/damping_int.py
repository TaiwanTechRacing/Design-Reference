import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# ==========================================
# Parameter setting
# ==========================================

m = 1.0        # mass (kg)
k = 50.0       # spring stiffness (N/m)
c = 2.0        # damping coefficient (N*s/m)
g = 9.81       # gravity (m/s^2)



# ==========================================
# Initial condition
# ==========================================

x0 = 0.1       # initial displacement (m)
v0 = 0.0       # initial velocity (m/s)



# ==========================================
# Simulation setting
# ==========================================

dt = 0.01

Tend = 10

N = int(np.floor(Tend / dt))


t = np.arange(
    0,
    N + 1
) * dt



# ==========================================
# Preallocate array
# ==========================================

x = np.zeros(
    N + 1
)

v = np.zeros(
    N + 1
)



# Initial value

x[0] = x0
v[0] = v0



# ==========================================
# Euler integration
# ==========================================

for i in range(N):

    # acceleration
    #
    # m*x'' + c*x' + k*x + mg = 0
    #

    a = (
        -c * v[i]
        - k * x[i]
        - m * g
    ) / m


    # update velocity

    v[i+1] = v[i] + a * dt


    # update displacement

    x[i+1] = x[i] + v[i] * dt



# ==========================================
# Plot
# ==========================================

plt.figure(
    figsize=(8,5)
)


plt.plot(
    t,
    x,
    linewidth=2
)


plt.xlabel(
    "Time (s)"
)


plt.ylabel(
    "Displacement x (m)"
)


plt.title(
    "Euler Integration Result (dt=0.01)"
)


plt.grid(True)



plt.tight_layout()



# ==========================================
# Save figure
# ==========================================

save_path = (
    Path(__file__).parent /
    "euler_mass_spring_response.png"
)


plt.savefig(
    save_path,
    dpi=300,
    bbox_inches="tight"
)


plt.show()


print(
    f"Figure saved to: {save_path}"
)