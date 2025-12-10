# Biologically-Inspired-Optimization-for-Scientific-Workflow-Scheduling-Using-Ant-Colony-Optimization


# Quick Start Guide

## 1. Check if Python is Installed

### Linux / macOS
```bash
python3 --version
```

### Windows
```powershell
python --version
```

### If Python is NOT installed

#### Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

#### macOS (Homebrew)
```bash
brew install python
```

#### Windows (Chocolatey)
```powershell
choco install python
```

---

## 2. Clone the Project

```bash
git clone https://github.com/azaharalam/Biologically-Inspired-Optimization-for-Scientific-Workflow-Scheduling-Using-Ant-Colony-Optimization
cd Biologically-Inspired-Optimization-for-Scientific-Workflow-Scheduling-Using-Ant-Colony-Optimization
```

---

## 3. Checkout to the Master Branch

```bash
git checkout master
```

---

## 4. Install Required Dependencies

If requirements.txt exists:
```bash
pip3 install -r requirements.txt
```

Otherwise manually install:
```bash
pip3 install numpy matplotlib networkx pandas tqdm
```

---

## 5. Run All Schedulers

```bash
python3 src/main.py
```

This runs:
- FIFO
- SJF
- Min-Min
- HEFT
- ACO

And prints makespan results.
