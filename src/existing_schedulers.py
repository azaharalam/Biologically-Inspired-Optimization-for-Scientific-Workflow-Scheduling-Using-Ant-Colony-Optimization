def min_min_scheduler(dag_dict, runtimes, num_machines=2):
    unscheduled = set(dag_dict.keys())
    machine_available = [0] * num_machines
    finish_times = {}
    schedule = []

    while unscheduled:
        # STEP 1 — find all READY tasks (parents finished)
        ready_tasks = []
        for t in unscheduled:
            parents = dag_dict[t]
            if all(p in finish_times for p in parents):
                ready_tasks.append(t)

        if not ready_tasks:
            raise RuntimeError("Deadlock detected: No ready tasks but unscheduled tasks remain.")

        # STEP 2 — compute earliest finish time for each ready task
        best_t = None
        best_m = None
        best_finish = float("inf")

        for t in ready_tasks:
            parent_finish = max([finish_times.get(p, 0) for p in dag_dict[t]] or [0])

            for m in range(num_machines):
                start = max(machine_available[m], parent_finish)
                finish = start + runtimes[t]

                if finish < best_finish:
                    best_finish = finish
                    best_t = t
                    best_m = m

        # STEP 3 — assign the best task
        start = best_finish - runtimes[best_t]
        finish_times[best_t] = best_finish
        machine_available[best_m] = best_finish

        schedule.append((best_t, best_m, start, best_finish))
        unscheduled.remove(best_t)

    makespan = max(machine_available)
    return schedule, makespan



def heft_scheduler(dag_dict, runtimes, num_machines=2):
    # Compute children
    children = {t: [] for t in dag_dict}
    for t, parents in dag_dict.items():
        for p in parents:
            children[p].append(t)

    # Compute upward rank
    rank_u = {}
    def compute_rank(t):
        if t in rank_u:
            return rank_u[t]
        if not children[t]:
            rank_u[t] = runtimes[t]
        else:
            rank_u[t] = runtimes[t] + max(compute_rank(c) for c in children[t])
        return rank_u[t]

    for t in dag_dict:
        compute_rank(t)

    ordered = sorted(dag_dict.keys(), key=lambda t: rank_u[t], reverse=True)

    finish_times = {}
    machine_available = [0] * num_machines
    schedule = []

    for t in ordered:
        parent_finish = max([finish_times.get(p, 0) for p in dag_dict[t]] or [0])

        best_m = None
        best_finish = float("inf")

        for m in range(num_machines):
            start = max(machine_available[m], parent_finish)
            finish = start + runtimes[t]
            if finish < best_finish:
                best_finish = finish
                best_m = m

        start = best_finish - runtimes[t]
        finish_times[t] = best_finish
        machine_available[best_m] = best_finish
        schedule.append((t, best_m, start, best_finish))

    return schedule, max(machine_available)
