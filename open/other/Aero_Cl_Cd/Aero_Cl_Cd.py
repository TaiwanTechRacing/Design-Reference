import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# Parameters
# ==========================================

rho = 1.225          # kg/m^3

w = 0.7              # m
h = 0.7              # m

A = w * h            # Reference area

F_ref = 700.0        # N
v_ref_kmh = 40     # km/h

# km/h -> m/s
v_ref = v_ref_kmh / 3.6

# ==========================================
# Lift coefficient
# ==========================================

Cl = F_ref / (0.5 * rho * A * v_ref**2)

print(f"Reference Lift Coefficient Cl = {Cl:.3f}")

# ==========================================
# Sweep speed
# ==========================================

v_kmh = np.linspace(0, 100, 201)

v = v_kmh / 3.6

# ==========================================
# Downforce
# ==========================================

F = 0.5 * Cl * rho * A * v**2

# ==========================================
# Plot
# ==========================================

plt.figure(figsize=(8,5))

plt.plot(
    v_kmh,
    F,
    linewidth=2,
    label="Downforce"
)

plt.scatter(
    [v_ref_kmh],
    [F_ref],
    color="red",
    zorder=5,
    label=f"Reference Point\n{F_ref:.1f}N\n{v_ref_kmh:.1f}km/h"
)

plt.xlabel("Vehicle Speed (km/h)")
plt.ylabel("Downforce (N)")
plt.title(f"Downforce vs Vehicle Speed")

plt.grid(True)
plt.legend()

# ==========================================
# Save
# ==========================================

output_dir = Path(__file__).parent

plt.savefig(
    output_dir / "downforce_vs_speed.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()