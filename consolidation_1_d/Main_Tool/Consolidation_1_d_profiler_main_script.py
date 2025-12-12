# A work done by Raúl Galdeano Pazos
# Isocrones Graphic Generator
# Geotechics
# December 2025

# ===========================================================

# I invoke some libraries that will be useful for this task:
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# To define the stated function to create the curves, function W(Z,T), which is a series solution.
# ============================================================

def W(Z, T, N_terms=50):

    Z = np.array(Z)
    T = np.array(T)
    Z, T = np.broadcast_arrays(Z, T)
    W_sum = np.zeros_like(Z, dtype=float)

    for n in range(N_terms):
        k = 2*n + 1                 
        coef = 4.0 / (k * np.pi)           
        exp_term = np.exp(- (np.pi**2 * k**2 / 4.0) * T)
        sin_term = np.sin((k * np.pi / 2.0) * Z)
        W_sum += coef * exp_term * sin_term

    return W_sum
# ============================================================
# Plot Generator Creation Space: 
# ============================================================

# I create a Z Space (Discretization): 

Z = np.linspace(0, 1, 200)

# Now, I put the demanded T values by the lectures, named as T_values, to draw the curves as most exact as possible:

T_values = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2]
plt.figure(figsize=(8, 6))

# The loop will iterate every value of T and N and will produce every correspondent curve according to the T value used:

for t in T_values:
    W_curve = W(Z, t, N_terms=80)
    plt.plot(W_curve, 1 - Z, label=f"T = {t}", linewidth = 2)

ax = plt.gca()
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
ax.grid(True, zorder=0)
ax.set_axisbelow(True)

plt.xlabel("W", fontweight = "bold")
plt.ylabel("1 - Z", fontweight = "bold")
plt.title("Curves of W(Z) based on different times (T)", fontweight = "bold")
plt.grid(False)
plt.legend()
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
plt.savefig("isocronas.pdf", dpi = 600)
