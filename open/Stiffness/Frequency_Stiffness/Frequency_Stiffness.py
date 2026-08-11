import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent

# Parameters
m = 260 / 2      # Quarter-car sprung mass (kg)
# Spring stiffness range
k = np.linspace(1000, 70000, 1000)    # N/m

# pitch 空力要求, pitch 行程要求, roll 空力要求, roll 行程要求
highlight_k = [42500, 34000,47700, 41000,]

# 計算
#=====================================
# Natural frequency
def natural_frequency(k,m):
    fn = (1 / (2 * np.pi)) * np.sqrt(k / m)
    return fn

fn = natural_frequency(k,m)#這邊計算應該要用ride rate

# =====================================
# Plot
plt.figure(figsize=(8, 5))

plt.plot(k / 1000,fn,linewidth=2)

for ki in highlight_k:
    fi = natural_frequency(ki,m)
    plt.scatter(ki / 1000, fi, color="red", zorder=5)

    plt.annotate(
        f"{fi:.2f} Hz",
        (ki / 1000, fi),
        xytext=(6, 8),
        textcoords="offset points"
    )

plt.grid(True)

plt.xlabel("Spring Stiffness (kN/m)")
plt.ylabel("Natural Frequency (Hz)")
plt.title("Natural Frequency vs Spring Stiffness")

plt.tight_layout()

# Save figure
output_path = OUTPUT_DIR / "Natural_Frequency_vs_Spring_Stiffness.png"

plt.savefig(output_path,dpi=300)

print(f"Figure saved to:\n{output_path}")

plt.show()



