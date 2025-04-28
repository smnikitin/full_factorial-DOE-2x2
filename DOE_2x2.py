# Import necessary libraries
import numpy as np  # Numerical operations
import tkinter as tk  # GUI library
from matplotlib.figure import Figure  # For creating figures for plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embed Matplotlib plots in Tkinter
import matplotlib.pyplot as plt  # Simplified plotting interface

# Function to calculate regression coefficients
def calculate_coefficients(Y, X1, X2):
    X = np.column_stack((np.ones(len(Y)), X1, X2, X1 * X2))  # Create matrix with constant, X1, X2, and their interaction
    coefficients = np.linalg.lstsq(X, Y, rcond=None)[0]  # Solve least squares for coefficients
    return coefficients  # Return calculated coefficients

# Function to calculate Y values from the equation using coefficients
def calculate_Y(coefficients, X1, X2):
    return coefficients[0] + coefficients[1] * X1 + coefficients[2] * X2 + coefficients[3] * X1 * X2  # Equation

# Function to plot a Pareto chart (bar chart of effects)
def plot_pareto_chart(coefficients):
    for widget in white_box1.winfo_children():  # Clear previous plots in white_box1
        widget.destroy()

    labels = ['X1', 'X2', 'X1 * X2']  # Labels for effects
    effects = np.abs(coefficients[1:])  # Absolute value of coefficients (excluding intercept)

    fig = Figure(figsize=(5, 4), dpi=80)  # Create a Matplotlib figure
    ax = fig.add_subplot(111)  # Add a subplot
    ax.barh(labels, effects, color='blue')  # Horizontal bar chart
    ax.set_title('Pareto Chart of the Effects', fontsize=14)  # Set title
    ax.set_xlabel('Effect', fontsize=12)  # Label x-axis
    ax.set_ylabel('Coefficients', fontsize=12)  # Label y-axis
    ax.grid(axis='x')  # Show grid on x-axis

    canvas = FigureCanvasTkAgg(fig, master=white_box1)  # Embed figure in Tkinter
    canvas.draw()  # Draw canvas
    canvas.get_tk_widget().pack()  # Pack canvas into white_box1

# Function to plot main effects of X1 and X2
def plot_effects(coefficients):
    X1_values = np.array([-1, 1])  # Range of X1
    X2_values = np.array([-1, 1])  # Range of X2

    Y_X1 = calculate_Y(coefficients, X1_values, np.zeros_like(X1_values))  # Y when X2 = 0
    Y_X2 = calculate_Y(coefficients, np.zeros_like(X2_values), X2_values)  # Y when X1 = 0

    for widget in white_box3.winfo_children():  # Clear previous plots in white_box3
        widget.destroy()

    fig, axs = plt.subplots(1, 2, figsize=(5, 2), sharey=True)  # Two side-by-side plots sharing Y-axis

    axs[0].plot(X1_values, Y_X1, 'o-', color='blue')  # Plot Y vs X1
    axs[0].set_title('Main Effects (Y vs X1)')  # Title
    axs[0].set_xlabel('X1')  # Label x-axis
    axs[0].set_ylabel('Y')  # Label y-axis
    axs[0].set_xticks(X1_values)  # Set x-ticks
    axs[0].grid()  # Enable grid

    axs[1].plot(X2_values, Y_X2, 'o-', color='blue')  # Plot Y vs X2
    axs[1].set_title('Main Effects (Y vs X2)')  # Title
    axs[1].set_xlabel('X2')  # Label x-axis
    axs[1].set_xticks(X2_values)  # Set x-ticks
    axs[1].grid()  # Enable grid

    max_y = max(np.max(Y_X1), np.max(Y_X2))  # Find maximum Y for scaling
    min_y = min(np.min(Y_X1), np.min(Y_X2))  # Find minimum Y for scaling
    axs[0].set_ylim(min_y - 0.1*(max_y-min_y), max_y + 0.1*(max_y-min_y))  # Set Y-limits with margin
    axs[1].set_ylim(min_y - 0.1*(max_y-min_y), max_y + 0.1*(max_y-min_y))  # Set Y-limits with margin

    canvas = FigureCanvasTkAgg(fig, master=white_box3)  # Embed figure in Tkinter
    canvas.draw()  # Draw canvas
    canvas.get_tk_widget().pack()  # Pack into white_box3

# Function to plot interaction lines
def plot_lines(coefficients):
    X1_values = np.array([-1, 1])  # Range for X1
    X2_values = np.array([-1, 1])  # Range for X2

    Y_X11 = calculate_Y(coefficients, X1_values, np.full_like(X1_values, -1))  # Y vs X1 when X2=-1
    Y_X12 = calculate_Y(coefficients, X1_values, np.full_like(X1_values, 1))   # Y vs X1 when X2=1
    Y_X21 = calculate_Y(coefficients, np.full_like(X2_values, -1), X2_values)  # Y vs X2 when X1=-1
    Y_X22 = calculate_Y(coefficients, np.full_like(X2_values, 1), X2_values)   # Y vs X2 when X1=1

    for widget in white_box2.winfo_children():  # Clear previous plots in white_box2
        widget.destroy()

    fig, axs = plt.subplots(1, 2, figsize=(5, 2), sharey=True)  # Two subplots side-by-side

    axs[0].plot(X1_values, Y_X11, 'o-', color='blue', label='X2 = -1')  # Plot for X2 = -1
    axs[0].plot(X1_values, Y_X12, 'o-', color='green', label='X2 = +1')  # Plot for X2 = +1
    axs[0].set_title('Interaction (X2: +/-)')  # Title
    axs[0].set_xlabel('X1')  # X-axis label
    axs[0].set_ylabel('Y')  # Y-axis label
    axs[0].legend()  # Add legend
    axs[0].set_xticks(X1_values)  # Set x-ticks
    axs[0].grid()  # Enable grid

    axs[1].plot(X2_values, Y_X21, 'o-', color='blue', label='X1 = -1')  # Plot for X1 = -1
    axs[1].plot(X2_values, Y_X22, 'o-', color='green', label='X1 = +1')  # Plot for X1 = +1
    axs[1].set_title('Interaction (X1: +/-)')  # Title
    axs[1].set_xlabel('X2')  # X-axis label
    axs[1].legend()  # Add legend
    axs[1].set_xticks(X2_values)  # Set x-ticks
    axs[1].grid()  # Enable grid

    max_y = max(np.max(Y_X11), np.max(Y_X12), np.max(Y_X21), np.max(Y_X22))  # Maximum Y value
    min_y = min(np.min(Y_X11), np.min(Y_X12), np.min(Y_X21), np.min(Y_X22))  # Minimum Y value
    axs[0].set_ylim(min_y - 0.1*(max_y-min_y), max_y + 0.1*(max_y-min_y))  # Y-axis limits
    axs[1].set_ylim(min_y - 0.1*(max_y-min_y), max_y + 0.1*(max_y-min_y))  # Y-axis limits

    canvas = FigureCanvasTkAgg(fig, master=white_box2)  # Embed figure in Tkinter
    canvas.draw()  # Draw canvas
    canvas.get_tk_widget().pack()  # Pack into white_box2

# Callback when "Calculate" button is clicked
def on_calculate():
    try:
        Y_values = [float(entry.get()) for entry in entries_Y]  # Get values from input fields
        Y = np.array(Y_values)  # Convert to NumPy array

        global coefficients  # Update global coefficients
        coefficients = calculate_coefficients(Y, X1, X2)  # Recalculate coefficients

        equation = f"Y = {coefficients[0]:.2f} + {coefficients[1]:.2f} * X1 + {coefficients[2]:.2f} * X2 + {coefficients[3]:.2f} * X1 * X2"
        equation_label.config(text=equation)  # Update label with new equation

        plot_pareto_chart(coefficients)  # Update Pareto plot
        plot_effects(coefficients)  # Update effects plot
        plot_lines(coefficients)  # Update interaction plot
        
    except ValueError:
        equation_label.config(text="Please enter valid numeric values for Y.")  # Handle non-numeric input

# Define X1 and X2 values for the design matrix
X1 = np.array([-1, 1, -1, 1])
X2 = np.array([-1, -1, 1, 1])

# Default Y values
default_Y_values = [1, 2, 3, 8]

Y = np.array(default_Y_values)  # Convert to array
coefficients = calculate_coefficients(Y, X1, X2)  # Initial coefficient calculation

# Initialize Tkinter GUI window
root = tk.Tk()
root.title("Calculate Equation Coefficients")  # Set window title

entries_Y = []  # List to hold entry widgets

# Create labels for table headers
tk.Label(root, text="X1", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="X2", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Y", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)

# Create entries for each row
for i in range(4):
    tk.Label(root, text=f"{X1[i]}", font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)  # X1 value
    tk.Label(root, text=f"{X2[i]}", font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)  # X2 value

    entry_Y = tk.Entry(root, width=10, font=("Arial", 12))  # Create Y input
    entry_Y.grid(row=i+1, column=2, padx=10, pady=5)  # Place Y input
    entry_Y.insert(0, str(default_Y_values[i]))  # Pre-fill with default value
    entries_Y.append(entry_Y)  # Save entry

# Button to trigger calculation
button = tk.Button(root, text="Calculate", command=on_calculate, font=("Arial", 12))
button.grid(row=5, columnspan=3, pady=10)

# Label to display the regression equation
equation_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white", width=40)
equation_label.grid(row=6, columnspan=3, padx=10, pady=10)

# Frame for the Pareto chart
white_box1 = tk.Frame(root, bg="white", width=500, height=300)
white_box1.grid(row=0, column=3, rowspan=7, padx=10, pady=10)

# Frame for the interaction plots
white_box2 = tk.Frame(root, bg="white", width=500, height=300)
white_box2.grid(row=7, column=3, padx=10, pady=10)

# Frame for the main effects plots
white_box3 = tk.Frame(root, bg="white", width=500, height=300)
white_box3.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Initial equation display
equation = f"Y = {coefficients[0]:.2f} + {coefficients[1]:.2f} * X1 + {coefficients[2]:.2f} * X2 + {coefficients[3]:.2f} * X1 * X2"
equation_label.config(text=equation)

# Initial plots
plot_pareto_chart(coefficients)
plot_effects(coefficients)
plot_lines(coefficients)

# Start the Tkinter event loop
root.mainloop()