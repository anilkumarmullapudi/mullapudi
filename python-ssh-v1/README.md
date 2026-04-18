# Parallel SSH Command Executor

This project provides a Python script to run commands on multiple servers in parallel using **Paramiko** and **ThreadPoolExecutor**.  
It is useful for Site Reliability Engineers, DevOps, or system administrators who need to quickly execute commands across multiple VMs or servers.

---

## íº€ Features
- Connects to multiple servers via SSH.
- Executes commands in parallel using threads.
- Captures both **stdout** and **stderr** outputs.
- Handles connection errors gracefully.
- Easy to extend for custom commands.

---

## í³‹ Requirements
- Python 3.7+
- Paramiko library

Install dependencies:
```bash
pip install paramiko

