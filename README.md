# 🔢 LA_Project: Matrix Norms & Condition Number Calculator

A robust Python tool for efficiently calculating various matrix norms and determining the condition number of matrices.

![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-None-lightgrey) ![Stars](https://img.shields.io/github/stars/kaifansariw/LA_Project?style=social) ![Forks](https://img.shields.io/github/forks/kaifansariw/LA_Project?style=social)

![Matrix Norms & Condition Number Calculator](/preview_example.png)


## ✨ Features

*   **📊 Comprehensive Norm Calculation:** Easily compute L1, L2 (spectral), Frobenius, and other p-norms for any given matrix.
*   **🔍 Condition Number Determination:** Accurately calculate the condition number, providing insights into matrix invertibility and numerical stability.
*   **🐍 Pure Python Implementation:** A lightweight and efficient solution built entirely in Python, ensuring broad compatibility.
*   **🚀 User-Friendly API:** Simple and intuitive functions make it straightforward to integrate into your linear algebra workflows.
*   **🧪 Robust & Tested:** Designed with accuracy in mind, providing reliable results for your mathematical computations.


## 🛠️ Installation

Follow these steps to get LA_Project up and running on your local machine.

### Prerequisites

Ensure you have Python 3.x installed.

### Manual Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kaifansariw/LA_Project.git
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd LA_Project
    ```
3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
5.  **Install the necessary dependencies:**
    ```bash
    pip install numpy
    ```

You are now ready to use `norms.py`!


## 🚀 Usage Examples

The `norms.py` module provides functions to calculate matrix norms and the condition number.

### Basic Usage

Here's how you can use the `LA_Project` to calculate norms and condition numbers:

```python
import numpy as np
from norms import calculate_norm, calculate_condition_number

# Define a sample matrix
matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])

matrix_c = np.array([[1, 1],
                     [1, 1]])

print("--- Matrix A ---")
print("Matrix:\n", matrix_a)
print("L1 Norm (Column Sum Norm):", calculate_norm(matrix_a, p=1))
print("L2 Norm (Spectral Norm):", calculate_norm(matrix_a, p=2))
print("Frobenius Norm:", calculate_norm(matrix_a, p='fro'))
print("Condition Number (L2):", calculate_condition_number(matrix_a, p=2))
print("-" * 20)

print("--- Matrix B (Identity Matrix) ---")
print("Matrix:\n", matrix_b)
print("L1 Norm:", calculate_norm(matrix_b, p=1))
print("L2 Norm:", calculate_norm(matrix_b, p=2))
print("Frobenius Norm:", calculate_norm(matrix_b, p='fro'))
print("Condition Number (L2):", calculate_condition_number(matrix_b, p=2))
print("-" * 20)

print("--- Matrix C (Singular Matrix) ---")
print("Matrix:\n", matrix_c)
print("L1 Norm:", calculate_norm(matrix_c, p=1))
print("L2 Norm:", calculate_norm(matrix_c, p=2))
# Condition number for singular matrix will be infinity
print("Condition Number (L2):", calculate_condition_number(matrix_c, p=2))
print("-" * 20)
```


## 🗺️ Project Roadmap

Our goal is to continually enhance the capabilities and usability of LA_Project. Here's what's planned for future versions:

*   **Version 1.1.0:**
    *   Add support for more specialized matrix norms (e.g., operator norms for specific vector norms).
    *   Implement better error handling for non-square matrices where applicable.
*   **Version 1.2.0:**
    *   Introduce a command-line interface (CLI) for quick calculations without writing Python scripts.
    *   Explore integration with `scipy.linalg` for potentially faster computations or broader norm support.
*   **Version 2.0.0:**
    *   Develop a comprehensive test suite to ensure robustness and accuracy across various matrix types.
    *   Documentation expansion with more mathematical context and examples.


## 🤝 Contribution Guidelines

We welcome contributions to LA_Project! To ensure a smooth collaboration, please follow these guidelines:

### Code Style

*   Adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
*   Use a linter like `flake8` and a formatter like `black` to maintain consistent code style.

### Branch Naming Conventions

*   For new features: `feature/<feature-name>` (e.g., `feature/add-infinity-norm`)
*   For bug fixes: `bugfix/<issue-description>` (e.g., `bugfix/singular-matrix-error`)
*   For documentation updates: `docs/<description>` (e.g., `docs/update-installation-guide`)

### Pull Request Process

1.  **Fork** the repository.
2.  **Create a new branch** from `main` (or `develop` if it exists).
3.  **Implement your changes** and ensure they are well-tested.
4.  **Commit your changes** with clear, descriptive commit messages.
5.  **Push your branch** to your forked repository.
6.  **Open a Pull Request** to the `main` branch of the original repository.
    *   Provide a clear description of your changes.
    *   Reference any relevant issues.

### Testing Requirements

*   All new features or bug fixes should include corresponding unit tests to verify functionality.
*   Ensure all existing tests pass before submitting a pull request.


## 📄 License Information

This project currently has **no specified license**.

**What this means:**
Without a license, the default copyright laws apply, meaning you (kaifansariw) retain all rights to your source code and no one may reproduce, distribute, or create derivative works from your work.

**Copyright Notice:**
© 2023 kaifansariw. All rights reserved.
