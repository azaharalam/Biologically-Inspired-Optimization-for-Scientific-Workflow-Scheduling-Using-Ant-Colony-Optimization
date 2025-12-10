import matplotlib.pyplot as plt

# Your final makespan values
makespans = {
    "FIFO": 4531.954,
    "SJF": 5901.126,
    "Min-Min": 4764.715,
    "HEFT": 2180.683,
    "ACO": 1903.091,
}

plt.figure(figsize=(10,6))
algorithms = list(makespans.keys())
values = list(makespans.values())

plt.plot(algorithms, values, marker='o', linewidth=3)

plt.title("Workflow Scheduling Makespan Comparison", fontsize=16)
plt.xlabel("Scheduling Algorithm", fontsize=14)
plt.ylabel("Makespan (seconds)", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("makespan_comparison.png", dpi=300)
plt.show()
