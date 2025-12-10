# Biologically-Inspired-Optimization-for-Scientific-Workflow-Scheduling-Using-Ant-Colony-Optimization


#📌 Overview

This repository contains the full implementation of a biologically inspired optimization framework for scientific workflow scheduling using Ant Colony Optimization (ACO). The project reproduces a complete evaluation pipeline used in the research paper:

Scheduling Montage workflow trace using five algorithms

Producing makespan comparisons

Generating convergence plots

Producing critical-path Gantt charts

Fully compiling the research LaTeX document

The implementation is dependency-aware, machine-aware, and designed to be run easily on Linux, macOS, or Windows.

🧠 Key Features
✅ Full ACO-based Scheduler

Dependency-aware task ordering

Earliest-finish-time machine assignment

Pheromone reinforcement & evaporation

Convergence logging

✅ Baseline Algorithms

FIFO

SJF

Min-Min

HEFT

✅ Visualization Suite

Makespan bar chart

Convergence curve

Critical-path Gantt chart

✅ Complete LaTeX Paper

IEEE conference style

Includes citations, figs, algorithms

📂 Project Structure
BioInspiredWorkflowACO/
│
├── README.md
├── src/
│   ├── main.py
│   ├── schedulers/
│   │   ├── aco_scheduler.py
│   │   ├── fifo.py
│   │   ├── sjf.py
│   │   ├── minmin.py
│   │   └── heft.py
│   ├── utils/
│   │   ├── dag_loader.py
│   │   └── plotting.py
│   └── analysis/
│       ├── gantt_chart.py
│       └── critical_path.py
│
├── figures/
│   ├── makespan_bar_chart.png
│   ├── convergence.png
│   └── gannt_chart.png
│
├── data/
│   └── tasks.json
│
├── paper/
│   ├── main.tex
│   └── refs.bib

🛠️ Installation

You can run this project on Linux, macOS, or Windows (with Python installed).

🔧 Step 1 — Install Python

Ensure Python 3.10+ is installed:

Linux/macOS:
python3 --version

Windows:
python --version


If Python is missing, install it from https://www.python.org
.

📦 Step 2 — Install Dependencies

From your project root directory:

pip install -r requirements.txt


If a requirements.txt is not generated yet, here is a good one:

numpy
matplotlib
networkx
pandas
tqdm

▶️ Running the Project
🏁 1. Run the schedulers and generate results
python3 src/main.py


This will:

Load tasks.json

Run FIFO, SJF, Min-Min, HEFT, and ACO

Save:

makespan_bar_chart.png

convergence.png

gannt_chart.png

Print the makespan summary to terminal
