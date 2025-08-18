# Environment Setup Guide

This guide will help you install **Miniconda**, set up **Python**, and run **Jupyter Notebooks** for numerical methods and chemical engineering coursework.

---

## 1. Install Miniconda

Miniconda is a lightweight distribution of **Conda**, a package manager that helps manage Python environments.

1.1 Download Miniconda:
   - [Miniconda Downloads](https://docs.conda.io/en/latest/miniconda.html)
   - Choose the installer for your OS (Windows, macOS, Linux).  
   - Recommended: **Python 3.x 64-bit** installer.

1.2. Install:
   - On Windows: run the `.exe` installer.
   - On macOS/Linux: run in terminal:
     ```
     bash Miniconda3-latest-Linux-x86_64.sh
     ```
   - Follow prompts and allow Conda to be added to your PATH.

1.3. Verify installation:
     ```
     conda --version
     pip --version
     ```

## 2. Create a Conda Environment

2.1 Create a separate environment for each project or course.

    ```bash
    conda create -n cpe701 python=3.10 -y
    ```
2.2 Then active it

    ```bash
    conda activate cpe701
    ```

2.3 Install Core Packages

    ```
    pip install numpy scipy matplotlib pandas sympy
    pip install notebook jupyterlab
    ```

2.4 Deactivate it 

    ```
    conda deactivate
    ```


