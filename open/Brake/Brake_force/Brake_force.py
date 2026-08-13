import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)

# =====================================
# Parameters
# =====================================

g = 9.81

m = 321 # 車重kg

mu_w = 1.7

r_w = 0.203          # m
r_disc_o = 0.21      # m
d_gap = 0.02         # m

mu_pad = 0.55

D_mc_f = 12e-3       # m
D_mc_r = 12e-3       # m

D_caliper_f = 34e-3  # m
D_caliper_r = 34e-3  # m

F_driver = 500.0     # N

balance_bar = 0.75
PR = 1.45

N_caliper_f = 2
N_caliper_r = 2

# =====================================
# Pedal Force
# =====================================

print(f"Driver Force = {F_driver:.2f} N")

F_mc = F_driver * PR

print(f"Master Cylinder Force = {F_mc:.2f} N")

# =====================================
# Balance Bar
# =====================================

bb_f = balance_bar
bb_r = 1.0 - balance_bar

# =====================================
# Master Cylinder Area
# =====================================

A_mc_f = np.pi * (D_mc_f / 2) ** 2
A_mc_r = np.pi * (D_mc_r / 2) ** 2

# =====================================
# Hydraulic Pressure
# =====================================

P_mc_f = F_mc * bb_f / A_mc_f
P_mc_r = F_mc * bb_r / A_mc_r

print(f"\nFront Line Pressure = {P_mc_f/1e6:.2f} MPa")
print(f"Rear  Line Pressure = {P_mc_r/1e6:.2f} MPa")

# =====================================
# Caliper Area
# =====================================

A_caliper_f = N_caliper_f * np.pi * (D_caliper_f / 2) ** 2
A_caliper_r = N_caliper_r * np.pi * (D_caliper_r / 2) ** 2

# =====================================
# Caliper Clamp Force
# =====================================

F_caliper_f = P_mc_f * A_caliper_f * mu_pad
F_caliper_r = P_mc_r * A_caliper_r * mu_pad

# =====================================
# Brake Force
# =====================================

r_disc = r_disc_o / 2 - d_gap

F_brake_f = F_caliper_f * r_disc * 2 / r_w
F_brake_r = F_caliper_r * r_disc * 2 / r_w

F_brake = F_brake_f + F_brake_r

# =====================================
# Results
# =====================================

print(f"\nFront Brake Force = {F_brake_f:.1f} N")
print(f"Rear  Brake Force = {F_brake_r:.1f} N")
print(f"Total Brake Force = {F_brake:.1f} N")

print(f"\nEquivalent Deceleration = {F_brake / g /m:.1f} g")

print("brake rate F : R =",F_brake_f/F_brake,":",F_brake_r/F_brake)
# unit brake rate

R_brake_f = F_brake_f/F_driver
R_brake_r = F_brake_r/F_driver

F_driver_list = np.linspace(0, 1000, 11)

F_brake_f_list = []
F_brake_r_list = []

for Fb in F_driver_list:
    F_brake_f = R_brake_f*Fb
    F_brake_r = R_brake_r*Fb

    F_brake_f_list.append(F_brake_f)
    F_brake_r_list.append(F_brake_r)


# plot
# ===============================================
F_brake_f_list = np.array(F_brake_f_list)
F_brake_r_list = np.array(F_brake_r_list)

F_brake_total_list = F_brake_f_list + F_brake_r_list

plt.figure(figsize=(8, 5))

plt.plot(
    F_driver_list,
    F_brake_f_list,
    "o-",
    linewidth=2,
    label="Front Brake Force"
)

plt.plot(
    F_driver_list,
    F_brake_r_list,
    "o-",
    linewidth=2,
    label="Rear Brake Force"
)

plt.plot(
    F_driver_list,
    F_brake_total_list,
    "k--",
    linewidth=2,
    label="Total Brake Force"
)

plt.grid(True)

plt.xlabel("Driver Pedal Force (N)")
plt.ylabel("Brake Force (N)")

plt.title("Brake Force vs Driver Pedal Force")

plt.legend()

plt.tight_layout()

output_path = OUTPUT_DIR / "Brake_force_vs_input_force.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# acc
# ========================================
a_list = F_brake_total_list / m
a_g_list = a_list / g

plt.figure(figsize=(8, 5))

plt.plot(
    F_driver_list,
    a_g_list,
    "o-",
    linewidth=2
)

plt.grid(True)

plt.xlabel("Driver Pedal Force (N)")
plt.ylabel("Deceleration (g)")

plt.title("Deceleration vs Driver Pedal Force")

plt.tight_layout()


output_path = OUTPUT_DIR / "Deceleration_vs_force.png"
plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
