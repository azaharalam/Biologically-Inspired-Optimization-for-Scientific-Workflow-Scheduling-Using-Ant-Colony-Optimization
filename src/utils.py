from collections import deque, defaultdict

def topological_sort(dag_dict):
    in_degree = defaultdict(int)
    for t, parents in dag_dict.items():
        in_degree[t] += 0
        for p in parents:
            in_degree[t] += 1

    q = deque([t for t in in_degree if in_degree[t] == 0])
    topo = []

    children = defaultdict(list)
    for t, parents in dag_dict.items():
        for p in parents:
            children[p].append(t)

    while q:
        t = q.popleft()
        topo.append(t)
        for c in children[t]:
            in_degree[c] -= 1
            if in_degree[c] == 0:
                q.append(c)

    if len(topo) != len(dag_dict):
        raise RuntimeError("Cycle detected in DAG. Not a valid workflow.")

    return topo


def get_ready_tasks(dag_dict, finish_times, unscheduled):
    ready = []
    for t in unscheduled:
        parents = dag_dict[t]
        if all(p in finish_times for p in parents):
            ready.append(t)
    return ready
