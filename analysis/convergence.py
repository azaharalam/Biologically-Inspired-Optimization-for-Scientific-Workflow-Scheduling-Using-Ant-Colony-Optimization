import matplotlib.pyplot as plt

# Best cost each iteration, EXACT DATA YOU PROVIDED
aco_costs = [
    1912.85, 1913.09, 1913.76, 1908.43, 1914.16,
    1916.75, 1912.96, 1918.88, 1914.72, 1913.40,
    1915.28, 1913.56, 1914.09, 1912.47, 1911.52,
    1912.62, 1916.34, 1917.05, 1914.67, 1915.31,
    1912.59, 1912.78, 1913.89, 1909.17, 1910.45,
    1914.30, 1908.94, 1912.22, 1905.90, 1904.28
]

iterations = list(range(1, 31))

plt.figure(figsize=(10,6))
plt.plot(iterations, aco_costs, marker='o', linewidth=2)

plt.title("ACO Convergence Curve", fontsize=16)
plt.xlabel("Iteration", fontsize=14)
plt.ylabel("Best Cost (Makespan)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("aco_convergence.png", dpi=300)
plt.show()
