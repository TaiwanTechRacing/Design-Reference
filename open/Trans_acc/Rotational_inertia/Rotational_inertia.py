import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


# =========================================================
# Output path
# =========================================================

OUTPUT_DIR = Path(__file__).resolve().parent

result_plot_path = OUTPUT_DIR / "gear_inertia_result.png"


# =========================================================
# Parameters
# =========================================================

T_values = np.array([20, 58, 24])   # Gear teeth
ad = np.array([0, 12, 12])          # Shaft diameter [mm]
h = np.array([20, 20, 10])           # Gear thickness [mm]

D = 7870                             # Density [kg/m^3]
N = 3

M = 0.8                              # Gear module [mm]

# Gear tooth numbers
Ts = 20
Tp1 = 58
Tp2 = 24
Tr = 102


# =========================================================
# Gear inertia calculation
# =========================================================

def gear_inertia(density, diameter, height):
    """
    Calculate rotational inertia of a solid cylindrical gear.

    Parameters
    ----------
    density : float
        Material density [kg/m^3]

    diameter : float
        Diameter [m]

    height : float
        Gear thickness [mm]

    Returns
    -------
    I : float
        Rotational inertia [kg*m^2]
    """

    r = diameter / 2

    area = np.pi * r**2

    # MATLAB h is given as mm,
    # convert to meters
    height_m = height / 1000

    volume = area * height_m

    mass = volume * density

    I = 0.5 * mass * r**2

    return I


# =========================================================
# Calculate inertia of each gear
# =========================================================

I_values = np.zeros(len(T_values))

for i in range(len(T_values)):

    # Gear diameter [mm]
    d = T_values[i] * M

    # Outer gear inertia
    I_outer = gear_inertia(
        D,
        d / 1000,
        h[i]
    )

    # Shaft hole inertia
    I_inner = gear_inertia(
        D,
        ad[i] / 1000,
        h[i]
    )

    # Actual gear inertia
    I_values[i] = I_outer - I_inner


# =========================================================
# Print individual gear inertia
# =========================================================

print("==============================")
print("Gear Rotational Inertia")
print("==============================")

for i, I in enumerate(I_values):

    print(
        f"Gear {i + 1}: "
        f"{I:.6e} kg*m^2"
    )


# =========================================================
# Gear ratio
# =========================================================

z2 = Tr / Tp2

z = Tp1 * z2 / Ts


print()
print("==============================")
print("Gear Ratio")
print("==============================")

print(f"z2 = {z2:.4f}")
print(f"z  = {z:.4f}")


# =========================================================
# Equivalent rotational inertia
# =========================================================

# Planet gear inertia reflected to the reference shaft
Ip = z2**2 * (
    I_values[1] + I_values[2]
)

# Sun gear inertia reflected to the reference shaft
Is = z**2 * I_values[0]


# =========================================================
# Total inertia
# =========================================================

I_all = Ip * N + Is


# =========================================================
# Results
# =========================================================

print()
print("==============================")
print("Equivalent Rotational Inertia")
print("==============================")

print(
    f"Planet gear inertia : "
    f"{Ip:.6e} kg*m^2"
)

print(
    f"Sun gear inertia    : "
    f"{Is:.6e} kg*m^2"
)

print(
    f"Total inertia       : "
    f"{I_all:.6e} kg*m^2"
)


# =========================================================
# Generate PNG
# =========================================================

fig, ax = plt.subplots(
    figsize=(9, 5)
)

ax.axis("off")

result_text = (
    "Gear Rotational Inertia\n"
    "\n"
    f"Gear 1 inertia       = {I_values[0]:.6e} kg·m²\n"
    f"Gear 2 inertia       = {I_values[1]:.6e} kg·m²\n"
    f"Gear 3 inertia       = {I_values[2]:.6e} kg·m²\n"
    "\n"
    f"z2                   = {z2:.4f}\n"
    f"z                    = {z:.4f}\n"
    "\n"
    f"Planet gear inertia  = {Ip:.6e} kg·m²\n"
    f"Sun gear inertia     = {Is:.6e} kg·m²\n"
    f"Total inertia        = {I_all:.6e} kg·m²"
)

ax.text(
    0.5,
    0.5,
    result_text,
    ha="center",
    va="center",
    fontsize=14,
    family="DejaVu Sans",
    transform=ax.transAxes
)

plt.tight_layout()

plt.savefig(
    result_plot_path,
    dpi=300,
    bbox_inches="tight"
)

print()
print(f"Result image saved to:")
print(result_plot_path)
