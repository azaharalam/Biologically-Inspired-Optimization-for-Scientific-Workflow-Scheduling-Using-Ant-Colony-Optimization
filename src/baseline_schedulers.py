def fifo_scheduler(dag_dict, runtimes, num_machines=2):
    unscheduled = set(dag_dict.keys())
    finish_times = {}
    machine_available = [0] * num_machines
    schedule = []

    while unscheduled:
        ready = [t for t in unscheduled if all(p in finish_times for p in dag_dict[t])]
        if not ready:
            raise RuntimeError("No ready tasks — DAG error.")

        t = ready[0]  # FIFO

        parent_finish = max([finish_times.get(p, 0) for p in dag_dict[t]] or [0])
        m = machine_available.index(min(machine_available))

        start = max(machine_available[m], parent_finish)
        finish = start + runtimes[t]

        finish_times[t] = finish
        machine_available[m] = finish
        schedule.append((t, m, start, finish))

        unscheduled.remove(t)

    return schedule, max(machine_available)




def shortest_job_first(dag_dict, runtimes, num_machines=2):
    unscheduled = set(dag_dict.keys())
    finish_times = {}
    machine_available = [0] * num_machines
    schedule = []

    while unscheduled:
        ready = [t for t in unscheduled if all(p in finish_times for p in dag_dict[t])]
        if not ready:
            raise RuntimeError("No ready tasks — DAG error.")

        t = min(ready, key=lambda x: runtimes[x])  # shortest runtime first

        parent_finish = max([finish_times.get(p, 0) for p in dag_dict[t]] or [0])
        m = machine_available.index(min(machine_available))
        start = max(machine_available[m], parent_finish)
        finish = start + runtimes[t]

        finish_times[t] = finish
        machine_available[m] = finish
        schedule.append((t, m, start, finish))
        unscheduled.remove(t)

    return schedule, max(machine_available)
