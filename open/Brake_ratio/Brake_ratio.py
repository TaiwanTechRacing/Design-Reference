import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent
OUTPUT_DIR.mkdir(exist_ok=True)


# Constants
g = 9.81

# Vehicle parameters
m = 320.0          # Vehicle mass (kg)

rf = 0.50          # Front weight distribution
rr = 0.50          # Rear weight distribution

h = 0.3           # CG height (m)
L = 1.53           # Wheelbase (m)

mu = 1.7           # Longitudinal friction coefficient

# 計算
# =====================================
# Static axle loads

Wf = rf * m * g
Wr = rr * m * g

# Deceleration sweep
a_g = np.linspace(0.1, mu, 10)      # g
a = a_g * g                         # m/s²


# Brake force calculation
Fb = m * a

dW = m * a * h / L

# Ideal front / rear brake force

Fbf = (Wf + dW) / (Wf + Wr) * Fb
Fbr = (Wr - dW) / (Wf + Wr) * Fb


# Linear regression through origin
k = np.sum(Fbf * Fbr) / np.sum(Fbf**2)

Fbf_fit = np.linspace(0, np.max(Fbf), 200)
Fbr_fit = k * Fbf_fit


# Equivalent balance bar ratio
bias_ratio = 1 / k

bias_ratio_f = bias_ratio / (bias_ratio + 1)
bias_ratio_r = 1 / (bias_ratio + 1)

print("=====================================")
print("Equivalent Brake Bias")
print("=====================================")
print(f"Front : Rear = {bias_ratio_f:.3f} : {bias_ratio_r:.3f}")
print(f"Front Bias = {bias_ratio_f*100:.1f}%")
print(f"Rear  Bias = {bias_ratio_r*100:.1f}%")


# Plot
# =====================================

plt.figure(figsize=(8, 6))

# Ideal brake curve
plt.plot(
    Fbf,
    Fbr,
    linewidth=2,
    label="Ideal Brake Curve"
)

# Regression line
plt.plot(
    Fbf_fit,
    Fbr_fit,
    "--",
    linewidth=2,
    label=f"Equivalent Balance Bar (Front : Rear = {bias_ratio_f:.3f} : {bias_ratio_r:.3f})"
)

# Mark each deceleration point
for x, y, ag in zip(Fbf, Fbr, a_g):
    plt.scatter(x, y, zorder=5)
    plt.text(
        x,
        y,
        f"{ag:.1f} g",
        fontsize=9,
        ha="left",
        va="bottom"
    )

plt.grid(True)

plt.xlabel("Front Brake Force $F_{bf}$ (N)")
plt.ylabel("Rear Brake Force $F_{br}$ (N)")

plt.title("Ideal Brake Force Distribution")

plt.legend()

plt.tight_layout()


# Save figure
# =====================================

output_path = OUTPUT_DIR / "Ideal_Brake_Bias.png"

plt.savefig(
    output_path,
    dpi=300,
    bbox_inches="tight"
)

print(f"\nFigure saved to:\n{output_path}")

plt.show()