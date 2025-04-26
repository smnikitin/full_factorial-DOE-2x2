# 📈 Two-Level Two - Factors Full Factorial simple DOE Tool

A simple Python-based GUI tool for calculating the coefficients of a **2x2 full factorial Design of Experiments (DOE)**, generating the fitted model, and visualizing the results through:

- A **Pareto chart** of the effects,
- Main effect **Y vs X1** and **Y vs X2** plots,
- Interaction plots for combined effects for Y.

Built with **Tkinter** for the GUI and **Matplotlib** for plotting.

---

## 📦 Requirements

- Python 3.x
- Tkinter
- NumPy
- maytplot

## ✨ Features

- Input custom **Y** values for a \(2^2\) factorial experiment.
- Automatically **calculate the regression coefficients** for the model:
  
```
Y = b0 + b1*X1 + b2*X2 + b12*X1*X2
```
  
- Visualize:
  - **Pareto Chart** (absolute effects),
  - **Main Effects** plots,
  - **Interaction** between factors.

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
git clone https://github.com/smnikitin/full_factorial-DOE-2x2.git
cd full_factorial-DOE-2x2
python DOE_2x2.py
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

## 📸 Screenshots

![demo1](https://github.com/smnikitin/face-detection/blob/main/img/Capture1.JPG) 

---

## 📂 Project Structure

```
full_factorial-DOE-2x2/
│
├── fDOE_2x2.py        # Main application 
├── README.md        # Project documentation
└── LICENSE        # (Optional)
└── img        # Screenshots
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

- Sergey Nikitin

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Credits

Created with 💻 using Python.  
Inspired by tutorials and open-source contributions from the computer vision community.

---

## 🤝 Contributing

Pull requests, feature suggestions, and issues are welcome! Let’s make this project even better together. ✨

