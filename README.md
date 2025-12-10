# Biologically-Inspired-Optimization-for-Scientific-Workflow-Scheduling-Using-Ant-Colony-Optimization


Biologically Inspired Workflow Scheduling using Ant Colony Optimization (ACO)

This repository contains a complete implementation of a biologically inspired optimization framework for scientific workflow scheduling using Ant Colony Optimization (ACO). The project includes:

Scheduling the Montage workflow trace using FIFO, SJF, Min-Min, HEFT, and ACO

Makespan comparison

Convergence plots

Critical-path Gantt chart

LaTeX paper (IEEE format) generation

The implementation supports Linux, macOS, and Windows.

Key Features
ACO-Based Scheduler

Dependency-aware task ordering

Earliest-finish-time machine assignment

Pheromone update + evaporation

Iteration-wise convergence logging

Baseline Algorithms

FIFO

SJF

Min-Min

HEFT

Visualization

Makespan bar chart

Convergence line plot

Gantt chart (critical-path annotated)

Research Paper

Full IEEE LaTeX paper (paper/main.tex)

Includes citations, equations, algorithms, and figures

Project Structure
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

Installation

You can run this project on Linux, macOS, or Windows.

1. Install Python

You need Python 3.10 or later.

Check your version:

Linux/macOS:

python3 --version


Windows:

python --version


If Python is missing, download it from:
https://www.python.org/downloads/

2. Install Dependencies

From the project root:

pip install -r requirements.txt


If you do not have a requirements.txt, you can create one containing:

numpy
matplotlib
networkx
pandas
tqdm

Running the Project
1. Run all schedulers and generate results
python3 src/main.py


This will:

Load the tasks.json workflow DAG

Execute FIFO, SJF, Min-Min, HEFT, and ACO

Generate plots:

makespan_bar_chart.png

convergence.png

gannt_chart.png

Print makespan comparison to the terminal
