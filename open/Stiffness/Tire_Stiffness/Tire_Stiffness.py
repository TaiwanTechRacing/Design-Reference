import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent

# Parameters
MR = 1                # Motion ratio
Kt = 100000.0             # Tire stiffness (N/m)

Ks = np.linspace(10000, 50000, 2000)   # Spring stiffness (N/m)

Kr_roll = 47700
Kr_heave = 42500
Kr_tag = (Kr_roll/2+Kr_heave/2)/2# 等校單輪剛性
"""
分析上需注意!!!

軸剛性>>輪剛性(/2)
單輪同時造成兩個彈簧壓縮因此平均剛性

軸剛性不等於彈簧剛性
F = k(彈簧剛性)*x(單輪抬升量)
單軸2輪力量*2倍壓縮輛等於4倍F
"""
# 計算
# =====================================
# Wheel rate
Kw = Ks * MR**2

# Ride rate
Kr = (Kw * Kt) / (Kw + Kt)


# =====================================
# Find target point
# =====================================

# Find spring stiffness corresponding to Kr_tag
idx_tag = np.argmin(np.abs(Kr - Kr_tag))

Ks_tag = Ks[idx_tag]
Kr_tag_actual = Kr[idx_tag]

k_rate = Kr_tag_actual / Ks_tag# 剛性修正

print(f"Target Ride Rate = {Kr_tag / 1000:.2f} kN/m")
print(f"Required Spring Rate = {Ks_tag / 1000:.2f} kN/m")
print(f"Actual Ride Rate = {Kr_tag_actual / 1000:.2f} kN/m")
print(f"k reduce rate = {k_rate:.2f} (Kr/Ks)")

# 計算實際修正量
Ks_roll = Kr_roll/k_rate
Ks_heave = Kr_heave/k_rate

Ks_actual = (Ks_roll/2+Ks_heave/2)/2# 等校單輪剛性
Kw_actual = Ks_actual*MR**2
Kr_actual = (Kw_actual * Kt) / (Kw_actual + Kt)

print(f"Ks_roll = {Ks_roll/1000:.2f} kN/m")
print(f"Ks_heave = {Ks_heave/1000:.2f} kN/m")
print(f"Kw_actual = {Kw_actual/1000:.2f} kN/m")
print(f"Kr_actual = {Kr_actual/1000:.2f} kN/m")
# Plot

# =====================================

plt.figure(figsize=(8, 5))

plt.plot(
    Ks / 1000,
    Kr / 1000,
    linewidth=2,
    label="Ride Rate"
)

# Reference line: without tire stiffness

plt.plot(
    Ks / 1000,
    Ks / 1000,
    linewidth=2,
    label="Spring Rate"
)

# Mark target point
plt.scatter(
    Ks_tag / 1000,
    Kr_tag_actual / 1000,
    color="red",
    s=80,
    zorder=5,
    label="Target"
)

plt.annotate(
    f"Ks = {Ks_tag/1000:.2f} kN/m\n"
    f"Kr = {Kr_tag_actual/1000:.2f} kN/m\n"
    f"Ks_roll = {Ks_roll/1000:.2f} kN/m\n"
    f"Ks_heave = {Ks_heave/1000:.2f} kN/m",
    xy=(Ks_tag / 1000, Kr_tag_actual / 1000),
    xytext=(20, 15),
    textcoords="offset points",
    arrowprops=dict(arrowstyle="->")
)

plt.grid(True)

plt.xlabel("Spring Rate (kN/m)")
plt.ylabel("Ride Rate (kN/m)")
plt.title("Spring Rate vs Ride Rate")

plt.legend()

plt.tight_layout()

# Save figure
# =====================================

output_path = OUTPUT_DIR / "Spring_Rate_vs_Ride_Rate.png"

plt.savefig(output_path, dpi=300)

print(f"Figure saved to:\n{output_path}")

plt.show()