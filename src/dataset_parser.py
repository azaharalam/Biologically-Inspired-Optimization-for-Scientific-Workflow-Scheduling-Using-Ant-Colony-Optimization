import json
import os

def load_wrench_montage_json(path):
    """
    Load a real WRENCH-Pegasus Montage workflow JSON file.
    Returns: dag_dict, runtimes
    """

    with open(path) as f:
        data = json.load(f)

    jobs = data["workflow"]["jobs"]

    dag_dict = {}
    runtimes = {}

    for job in jobs:
        name = job["name"]
        parents = job.get("parents", [])
        runtime = job.get("runtime", 1.0)  # fallback

        dag_dict[name] = parents
        runtimes[name] = float(runtime)

    return dag_dict, runtimes
