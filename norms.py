 
import tkinter as tk
from tkinter import messagebox
import numpy as np

def parse_matrix(input_str):
    try:
        matrix = np.array(eval(input_str), dtype=float)
        if len(matrix.shape) != 2:
            raise ValueError
        return matrix
    except:
        raise ValueError("Invalid matrix format. Use Python-style lists (e.g., [[1, 2], [3, 4]])")

def calculate_norms():
    try:
        A = parse_matrix(matrix_input.get("1.0", tk.END).strip())

        if A.shape[0] != A.shape[1]:
            raise ValueError("Matrix must be square.")

        results = []
        norms = {
            '1-norm': np.linalg.norm(A, 1),
            '2-norm (spectral)': np.linalg.norm(A, 2),
            '∞-norm': np.linalg.norm(A, np.inf),
            'Frobenius norm': np.linalg.norm(A, 'fro')
        }

        for name, value in norms.items():
            try:
                cond = np.linalg.cond(A, p={'1-norm': 1, '2-norm (spectral)': 2, '∞-norm': np.inf, 'Frobenius norm': 'fro'}[name])
            except np.linalg.LinAlgError:
                cond = 'Undefined (singular matrix)'
            results.append(f"{name}: {value:.4f} | Condition number: {cond if isinstance(cond, str) else f'{cond:.4f}'}")

        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, "\n".join(results))

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Matrix Norms & Condition Number Calculator")

tk.Label(root, text="Enter matrix (e.g. [[1, 2], [3, 4]]):").pack()
matrix_input = tk.Text(root, height=5, width=40)
matrix_input.pack()

tk.Button(root, text="Calculate Norms & Condition Numbers", command=calculate_norms).pack(pady=10)

tk.Label(root, text="Results:").pack()
result_output = tk.Text(root, height=10, width=60)
result_output.pack()

root.mainloop()

































