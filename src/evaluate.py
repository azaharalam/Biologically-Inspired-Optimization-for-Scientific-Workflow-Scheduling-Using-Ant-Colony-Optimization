def print_schedule(name, schedule, makespan):
    print(f"\n{name} Schedule:")
    print("Task | Machine | Start     | Finish")
    for t, m, s, f in schedule[:20]:   # showing only first 20 for readability
        print(f"{t:20s} | {m:7d} | {s:8.2f} | {f:8.2f}")
    print(f"\n{name} Makespan = {makespan:.2f}\n")
