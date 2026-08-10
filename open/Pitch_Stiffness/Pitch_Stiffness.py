import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Constants
g = 9.81

# Vehicle data
m = 321          # kg
a = 1.6          # acceleration (g)
h = 0.3         # CG height (m)
L = 1.53         # wheelbase (m)
target_theta = 1.5

# Allowable pitch angle sweep
theta_deg = np.arange(0.1, 3.1, 0.1)
theta = np.deg2rad(theta_deg)


# 計算
# =============================================
# Chassis displacement at axle
s = (L / 2) * theta



# Pitch moment
Fx = m * a * g
M = Fx * h
F = M / (L / 2)

# Required stiffness
K = F / (2 * s)


# Find stiffness
idx = np.argmin(np.abs(theta_deg - target_theta))
K_target = K[idx]

print(f"Pitch stiffness @ {target_theta:.1f}° = {K_target:.1f} N/m")

# 計算目標行程
target_s = (L / 2) * np.deg2rad(target_theta)
print(f"Target displacement @ {target_theta:.1f}° = {target_s:.3f} m")

# Plot
# ============================================
plt.figure(figsize=(8, 5))

plt.plot(K, theta_deg, linewidth=2, label="Requirement")

# Mark 1.5 degree
plt.scatter(K_target, target_theta,
            color="red",
            s=80,
            zorder=5)

plt.annotate(
    f"{K_target:,.0f} N/m\n@ {target_theta:.1f}°",
    xy=(K_target, target_theta),
    xytext=(20, 10),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.grid(True)
plt.xlabel("Pitch Stiffness K (N/m)")
plt.ylabel("Allowable Pitch Angle (deg)")
plt.title("Pitch Stiffness Requirement vs Allowable Pitch Angle")

plt.tight_layout()


# Save figure
output_path = Path(__file__).parent / "Pitch_Stiffness_Requirement.png"

plt.savefig(output_path, dpi=300)

print(f"Figure saved to:\n{output_path}")

plt.show()