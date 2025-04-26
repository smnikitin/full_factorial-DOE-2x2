# 📈 Two-Level Full Factorial DOE Tool

A simple Python-based GUI tool for calculating the coefficients of a **two-level full factorial Design of Experiments (DOE)**, generating the fitted model, and visualizing the results through:

- A **Pareto chart** of effects,
- **Y vs X1** and **Y vs X2** plots,
- Interaction plots for combined effects.

Built with **Tkinter** for the GUI and **Matplotlib** for plotting.

---

## ✨ Features

- Input custom **Y** values for a \(2^2\) factorial experiment.
- Automatically **calculate the regression coefficients** for the model:
  
  \[
  Y = b_0 + b_1X_1 + b_2X_2 + b_{12}X_1X_2
  \]
  
- Visualize:
  - **Pareto Chart** (absolute effects),
  - **Main Effects** plots,
  - **Interaction Lines** between factors.

---

## 🛠️ Installation

Make sure you have Python 3 installed.

Install the required Python libraries:

```bash
pip install numpy matplotlib
```

No external libraries for the GUI — Tkinter is included with standard Python installations.

---

## 🚀 How to Run

Clone the repository and run the script:

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
python factorial_doe_tool.py
```

A window will open where you can:

- Edit the Y values,
- Click **"Calculate"** to update the model and plots.

---

## 📊 Example

Given inputs:

| X1  | X2  | Y (output) |
|:---:|:---:|:----------:|
| -1  | -1  | 1          |
|  1  | -1  | 2          |
| -1  |  1  | 3          |
|  1  |  1  | 8          |

The tool computes and displays the fitted model:

```
Y = b0 + b1*X1 + b2*X2 + b12*X1*X2
```

and updates the plots accordingly.

---

## 📂 Project Structure

```
factorial_doe_tool.py  # Main Python file containing all functionality
README.md              # Project documentation
```

---

## 🧠 Behind the Scenes

- **Regression Calculation**: Least squares solution using NumPy.
- **GUI**: Built with Tkinter.
- **Plots**: Rendered dynamically using Matplotlib inside the Tkinter frames.
- **Design**: Focused on clear interaction and real-time feedback.

---

## ⚡ Future Improvements

- Extend to **\(2^k\)** factorial designs.
- Add **confidence intervals** on effects.
- Allow saving plots.
- Add coded/uncoded factor conversion.

---

## 🧑‍💻 Author

- [Your Name](https://github.com/yourusername)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

Would you also like me to show you how it could look if you want a slightly **shorter** or more **casual** version depending on your GitHub style? 🚀  
(Also, I can make a simple badge section if you want it to look extra professional!) 🎨
