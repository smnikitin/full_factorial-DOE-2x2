# 📈 Two-Level Two-Factor Full Factorial DOE Tool

A simple Python-based GUI tool for calculating the coefficients of a **2×2 full factorial Design of Experiments (DOE)**, generating the fitted model, and visualizing the results through:

- A **Pareto chart** of effects,
- Main effect **Y vs X1** and **Y vs X2** plots,
- **Interaction plots** for combined effects.

Built with **Tkinter** for the GUI and **Matplotlib** for plotting.

---

## 📦 Requirements

- Python 3.x
- Tkinter (comes with Python)
- NumPy
- Matplotlib

## ✨ Features

- Input custom **Y** values for a \(2^2\) factorial experiment.
- Automatically **calculate regression coefficients** for the model:

```math
Y = b0 + b1 * X1 + b2 * X2 + b12 * X1 * X2
```

- Visualize:
  - **Pareto chart** of absolute effects,
  - **Main effects** plots,
  - **Interaction effects** plots.

---

## 🚫 Not Included

- ANOVA analysis,
- Model evaluation metrics (e.g., R², RMSE),
- Prediction of **X** values for a given **Y**.

---

## 🛠️ Installation

Make sure you have Python 3 installed.

Install the required Python libraries:

```bash
pip install numpy matplotlib
```

No external libraries are needed for the GUI — **Tkinter** is included with standard Python distributions.

---

## 🚀 How to Run

Clone the repository and run the script:

```bash
git clone https://github.com/smnikitin/full_factorial-DOE-2x2.git
cd full_factorial-DOE-2x2
python DOE_2x2.py
```

A window will open where you can:

- Edit the Y values,
- Click **"Calculate"** to update the model and refresh the plots.

---

## 📊 Example

Given inputs:

| X1  | X2  | Y (output) |
|:---:|:---:|:----------:|
| -1  | -1  | 1          |
|  1  | -1  | 2          |
| -1  |  1  | 3          |
|  1  |  1  | 8          |

The tool calculates and displays the fitted model:

```math
Y = b0 + b1 * X1 + b2 * X2 + b12 * X1 * X2
```

and updates all plots accordingly.

---

## 📸 Screenshots

![demo1](https://github.com/smnikitin/full_factorial-DOE-2x2/blob/main/img/Capture3.JPG)

---

## 📂 Project Structure

```
full_factorial-DOE-2x2/
│
├── DOE_2x2.py        # Main application
├── README.md         # Project documentation
├── LICENSE           # (Optional)
└── img/              # Screenshots folder
```

---

## 🧠 Behind the Scenes

- **Regression Calculation**: Solved via least squares using NumPy.
- **GUI**: Built with Tkinter for a lightweight, native interface.
- **Plots**: Generated dynamically using Matplotlib and embedded in the GUI.
- **Design**: Focused on ease of use, clean visuals, and real-time interaction.

---

## ⚡ Future Improvements

- Extend functionality to **\(2^k\)** full factorial designs.
- Add **confidence intervals** and **error bars** for effects.
- Allow saving plots as images.
- Implement **coded/uncoded factor** conversions.

---

## 🧑‍💻 Author

- Sergey Nikitin

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Created with 💻 using Python.  
Inspired by open-source tutorials and the broader Python development community.

---

## 🤝 Contributing

Pull requests, suggestions, and feedback are welcome!  
Let’s make this project even better together. ✨
