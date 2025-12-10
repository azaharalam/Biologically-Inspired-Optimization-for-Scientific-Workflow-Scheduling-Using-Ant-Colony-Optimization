import random
from utils import topological_sort


class ACO_Scheduler:

    def __init__(self, dag_dict, runtimes, num_ants=20, iterations=30,
                 num_machines=2, alpha=1.0, beta=2.0, evaporation=0.1):

        self.dag = dag_dict
        self.runtimes = runtimes
        self.num_ants = num_ants
        self.iterations = iterations
        self.num_machines = num_machines

        # ACO hyperparameters
        self.alpha = alpha        # pheromone exponent
        self.beta = beta          # heuristic exponent
        self.evaporation = evaporation

        # Pheromone initialization
        self.pheromone = {t: 1.0 for t in self.dag.keys()}

        self.rank_u = self._compute_upward_ranks()

        self.machine_speed = [1.0, 1.2, 0.9, 1.5]




    # ---------------------------------------------------------
    # TASK SELECTION FUNCTION (ACO PROBABILISTIC CHOICE)
    # ---------------------------------------------------------
    def _choose_task(self, ready_tasks):
        """
        Choose next task probabilistically based on pheromone + heuristic.
        """
        weights = []

        for t in ready_tasks:
            tau = self.pheromone.get(t, 1.0)
            eta = self.rank_u[t]

            w = (tau ** self.alpha) * (eta ** self.beta)
            weights.append(w)

        total = sum(weights)
        probs = [w / total for w in weights]

        return random.choices(ready_tasks, weights=probs, k=1)[0]


    def _compute_upward_ranks(self):
        children = {t: [] for t in self.dag}
        for t, parents in self.dag.items():
            for p in parents:
                children[p].append(t)

        rank_u = {}

        def compute_rank(t):
            if t in rank_u:
                return rank_u[t]
            if not children[t]:
                rank_u[t] = self.runtimes[t]
            else:
                rank_u[t] = self.runtimes[t] + max(compute_rank(c) for c in children[t])
            return rank_u[t]

        for t in self.dag:
            compute_rank(t)

        return rank_u


    # ---------------------------------------------------------
    # BUILD A COMPLETE SCHEDULE PER ANT
    # ---------------------------------------------------------
    def _construct_solution(self):
        unscheduled = set(self.dag.keys())
        finish_times = {}
        machine_available = [0] * self.num_machines
        schedule = []

        while unscheduled:
            # tasks whose parents are all completed
            ready = [t for t in unscheduled if all(p in finish_times for p in self.dag[t])]
            if not ready:
                raise RuntimeError("No ready tasks available — DAG cycle or missing parent.")

            # probabilistically choose next task
            t = self._choose_task(ready)

            # compute earliest start time based on parents & machine
            parent_finish = max([finish_times.get(p, 0) for p in self.dag[t]] or [0])

            best_m = None
            best_finish = float("inf")

            for m in range(self.num_machines):
                start = max(machine_available[m], parent_finish)
                finish = start + (self.runtimes[t]/self.machine_speed[m])

                if finish < best_finish:
                    best_finish = finish
                    best_m = m

            start = best_finish - self.runtimes[t]
            finish_times[t] = best_finish
            machine_available[best_m] = best_finish

            schedule.append((t, best_m, start, best_finish))

            unscheduled.remove(t)

        makespan = max(machine_available)
        return schedule, makespan


    # ---------------------------------------------------------
    # MAIN ACO LOOP
    # ---------------------------------------------------------
    def run(self):
        best_schedule = None
        best_cost = float("inf")

        for it in range(self.iterations):
            iteration_best_cost = float("inf")
            iteration_best_schedule = None

            for _ in range(self.num_ants):
                sched, cost = self._construct_solution()

                if cost < iteration_best_cost:
                    iteration_best_cost = cost
                    iteration_best_schedule = sched

                if cost < best_cost:
                    best_cost = cost
                    best_schedule = sched

            # ------------------------------------
            # PHEROMONE UPDATE (EVAPORATE + DEPOSIT)
            # ------------------------------------
            for t in self.pheromone:
                self.pheromone[t] *= (1 - self.evaporation)

            # deposit pheromone on tasks in best schedule of this iteration
            for t, m, s, f in iteration_best_schedule:
                self.pheromone[t] += 1.0 / (1.0 + iteration_best_cost)

            print(f"Iteration {it+1}/{self.iterations} — best cost this iter: {iteration_best_cost:.2f}")

        return best_schedule, best_cost
