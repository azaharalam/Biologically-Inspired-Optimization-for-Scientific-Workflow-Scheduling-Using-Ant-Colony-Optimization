import matplotlib.pyplot as plt
from collections import defaultdict

def compute_rank_u(dag, runtimes):
    children = defaultdict(list)
    for t, parents in dag.items():
        for p in parents:
            children[p].append(t)

    rank_u = {}

    def dfs(t):
        if t in rank_u:
            return rank_u[t]
        if not children[t]:
            rank_u[t] = runtimes[t]
        else:
            rank_u[t] = runtimes[t] + max(dfs(c) for c in children[t])
        return rank_u[t]

    for t in dag:
        dfs(t)
    return rank_u

def extract_critical_path(dag, runtimes):
    rank_u = compute_rank_u(dag, runtimes)
    start = max(rank_u, key=lambda x: rank_u[x])

    path = [start]
    node = start

    while True:
        children = [c for c, parents in dag.items() if node in parents]
        if not children:
            break
        next_child = max(children, key=lambda x: rank_u[x])
        path.append(next_child)
        node = next_child
    
    return path

def plot_gantt(schedule, critical_tasks):
    # Filter entries only for critical-path tasks
    sched = [s for s in schedule if s[0] in critical_tasks]

    plt.figure(figsize=(12,7))

    for i, (task, m, start, finish) in enumerate(sched):
        plt.barh(task, finish - start, left=start, height=0.4)

    plt.xlabel("Time (seconds)")
    plt.ylabel("Critical Path Tasks")
    plt.title("Gantt Chart for Critical Path")
    plt.grid(True, linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.savefig("critical_path_gantt.png", dpi=300)
    plt.show()
