import json
import os,sys

from aco_scheduler import ACO_Scheduler
from baseline_schedulers import fifo_scheduler, shortest_job_first
from existing_schedulers import min_min_scheduler, heft_scheduler
from evaluate import print_schedule
from dataset_parser import load_wrench_montage_json


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT)

from analysis.gannt_chart import extract_critical_path, plot_gantt


def load_dataset():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(base_dir)
    dataset_dir = os.path.join(project_dir, "dataset")

    json_path = os.path.join(dataset_dir, "montage-chameleon.json")

    print("Looking for dataset at:", json_path)

    print(load_wrench_montage_json(json_path))

    return load_wrench_montage_json(json_path)

def run_all_schedulers(dag_dict, runtimes, num_machines=4):
    results = {}

    print("\n==========================================")
    print("            RUNNING FIFO")
    print("==========================================")
    fifo_sched, fifo_cost = fifo_scheduler(dag_dict, runtimes, num_machines)
    print_schedule("FIFO", fifo_sched, fifo_cost)
    results["FIFO"] = fifo_cost

    print("\n==========================================")
    print("            RUNNING SJF")
    print("==========================================")
    sjf_sched, sjf_cost = shortest_job_first(dag_dict, runtimes, num_machines)
    print_schedule("SJF", sjf_sched, sjf_cost)
    results["SJF"] = sjf_cost

    print("\n==========================================")
    print("            RUNNING MIN-MIN")
    print("==========================================")
    minmin_sched, minmin_cost = min_min_scheduler(dag_dict, runtimes, num_machines)
    print_schedule("Min-Min", minmin_sched, minmin_cost)
    results["Min-Min"] = minmin_cost

    print("\n==========================================")
    print("            RUNNING HEFT")
    print("==========================================")
    heft_sched, heft_cost = heft_scheduler(dag_dict, runtimes, num_machines)
    print_schedule("HEFT", heft_sched, heft_cost)
    results["HEFT"] = heft_cost

    print("\n==========================================")
    print("            RUNNING ACO")
    print("==========================================")
    aco = ACO_Scheduler(
        dag_dict,
        runtimes,
        alpha=1.0,
        beta=3.0,
        evaporation=0.05,
        num_ants=40,
        iterations=30,
        num_machines=num_machines
    )
    best_sched, best_cost = aco.run()
    #critical = extract_critical_path(dag_dict, runtimes)
    #plot_gantt(best_sched, critical)
    print_schedule("ACO", best_sched, best_cost)
    results["ACO"] = best_cost

    return results


def print_summary(results):
    print("\n\n==========================================")
    print("              FINAL SUMMARY")
    print("==========================================")
    for alg, cost in results.items():
        print(f"{alg:10s} → Makespan = {cost}")


if __name__ == "__main__":
    dag_dict, runtimes = load_dataset()


    results = run_all_schedulers(dag_dict, runtimes, num_machines=4)
    print_summary(results)
