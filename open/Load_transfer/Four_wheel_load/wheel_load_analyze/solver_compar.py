import numpy as np
import matplotlib.pyplot as plt
from types import SimpleNamespace
from FWL_solver import four_wheel_load_cg, four_wheel_load_lsm

# =====================================
# Vehicle parameters
# =====================================

g = 9.81

car = SimpleNamespace(
    m=321.0,
    h=0.30,
    L=1.53,
    d=1.25,
    CG_x=np.array([0.48, 0.52]),   # Front / Rear
    CG_y=np.array([0.50, 0.50])    # Left / Right
)

# =====================================
# Vehicle state
# =====================================

ax = 2 * g
ay = 2 * g

# =====================================
# External force
# =====================================

F_add = np.array([
    0.0,
    0.0,
    0.0
])

CF_rela = np.array([
    0.0,
    0.0,
    0.0
])

# =====================================
# Compute wheel loads
# =====================================

N1 = four_wheel_load_lsm(
    ax=ax,
    ay=ay,
    F_add=F_add,
    CF_rela=CF_rela,
    car=car,
    check=True
)

N2 = four_wheel_load_cg(
    ax=ax,
    ay=ay,
    F_add=F_add,
    CF_rela=CF_rela,
    car=car,
    check=True
)

delta = np.abs(N1 - N2)

# =====================================
# Plot
# =====================================

wheel_labels = ["FL", "FR", "RL", "RR"]

x = np.arange(len(wheel_labels))
bar_width = 0.25

plt.figure(figsize=(8, 5))

plt.bar(
    x - bar_width,
    N1,
    width=bar_width,
    label="LSM"
)

plt.bar(
    x + bar_width,
    N2,
    width=bar_width,
    label="CG Ratio"
)

plt.bar(
    x,
    delta,
    width=bar_width,
    label="Difference"
)

plt.xticks(x, wheel_labels)

plt.ylabel("Wheel Load (N)")
plt.title("Comparison of Four Wheel Loads")

plt.grid(axis="y")
plt.legend()

plt.tight_layout()
plt.show()

# null space
# ====================================
import numpy as np
import matplotlib.pyplot as plt
from types import SimpleNamespace


# =====================================
# Vehicle
# =====================================

g = 9.81

car = SimpleNamespace(
    m=321,
    h=0.30,
    L=1.53,
    d=1.25,

    CG_x=np.array([0.48,0.52]),
    CG_y=np.array([0.5,0.5])
)


F_add = np.zeros(3)
CF_rela = np.zeros(3)



# =====================================
# Lateral acceleration sweep
# =====================================

ax = 0.0

ay_range = np.linspace(
    0,
    2*g,
    100
)



# =====================================
# Storage
# =====================================

N_lsm = np.zeros(
    (len(ay_range),4)
)

N_cg = np.zeros(
    (len(ay_range),4)
)

V = np.zeros(
    (len(ay_range),4)
)



# =====================================
# Calculate
# =====================================
# =====================================
# Storage
# =====================================

N_lsm = np.zeros(
    (len(ay_range),4)
)

N_cg = np.zeros(
    (len(ay_range),4)
)

V = np.zeros(
    (len(ay_range),4)
)


alpha_min = np.zeros(len(ay_range))
alpha_max = np.zeros(len(ay_range))


alpha_min_list = np.zeros(len(ay_range))
alpha_max_list = np.zeros(len(ay_range))
# =====================================
# Calculate
# =====================================

for i, ay in enumerate(ay_range):


    N1 = four_wheel_load_lsm(
        ax,
        ay,
        F_add,
        CF_rela,
        car,
        False
    )


    N2 = four_wheel_load_cg(
        ax,
        ay,
        F_add,
        CF_rela,
        car,
        False
    )


    V_i = N2 - N1


    N_lsm[i] = N1
    N_cg[i] = N2
    V[i] = V_i


    # ------------------------------
    # Find alpha range
    # ------------------------------

    amin = -np.inf
    amax = np.inf


    for wheel in range(4):

        n = N1[wheel]
        v = V_i[wheel]


        # null direction = 0
        if abs(v) < 1e-12:
            continue


        limit = -n / v


        if v > 0:

            # alpha > limit
            amin = max(
                amin,
                limit
            )


        else:

            # alpha < limit
            amax = min(
                amax,
                limit
            )


    alpha_min[i] = amin
    alpha_max[i] = amax


# =====================================
# Plot wheel load
# =====================================

wheel_name = [
    "FL",
    "FR",
    "RL",
    "RR"
]


plt.figure(figsize=(8,5))


for i in range(4):

    plt.plot(
        ay_range/g,
        N_lsm[:,i],
        label=f"{wheel_name[i]} LSM"
    )


plt.xlabel(
    "ay (g)"
)

plt.ylabel(
    "Wheel Load (N)"
)

plt.title(
    "Wheel Load vs Lateral Acceleration"
)

plt.grid()
plt.legend()

plt.show()



# =====================================
# Plot null space direction
# =====================================

plt.figure(figsize=(8,5))


for i in range(4):

    plt.plot(
        ay_range/g,
        V[:,i],
        label=wheel_name[i]
    )


plt.axhline(
    0,
    color="black"
)


plt.xlabel(
    "ay (g)"
)

plt.ylabel(
    "Null Space Direction ΔN (N)"
)


plt.title(
    "Null Space Direction vs Lateral Acceleration"
)


plt.grid()
plt.legend()

plt.show()

plt.figure(figsize=(8,5))


plt.plot(
    ay_range/g,
    alpha_min,
    label="alpha min"
)


plt.plot(
    ay_range/g,
    alpha_max,
    label="alpha max"
)


plt.fill_between(
    ay_range/g,
    alpha_min,
    alpha_max,
    alpha=0.3
)


plt.xlabel(
    "ay (g)"
)

plt.ylabel(
    "Allowable alpha"
)


plt.title(
    "Null Space Feasible Region"
)


plt.grid()
plt.legend()

plt.show()