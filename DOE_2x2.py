import numpy as np
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt  # Import matplotlib for additional plots

# Function to calculate coefficients based on input Y values
def calculate_coefficients(Y, X1, X2):
    X = np.column_stack((np.ones(len(Y)), X1, X2, X1 * X2))
    coefficients = np.linalg.lstsq(X, Y, rcond=None)[0]
    return coefficients


# Function to calculate Y values based on the given equation coefficients
def calculate_Y(coefficients, X1, X2):
    return coefficients[0] + coefficients[1] * X1 + coefficients[2] * X2 + coefficients[3] * X1 * X2


# Function to plot Pareto chart of effects
def plot_pareto_chart(coefficients):
    # Clear the previous plot
    for widget in white_box1.winfo_children():
        widget.destroy()

    labels = ['X1', 'X2', 'X1 * X2']  # Updated labels
    effects = np.abs(coefficients[1:])  # Use absolute values for the Pareto chart

    # Create a new figure for the plot with increased height and width
    fig = Figure(figsize=(5, 4), dpi=80)  # Increased size for better visibility
    ax = fig.add_subplot(111)

    # Create a horizontal bar chart
    ax.barh(labels, effects, color='blue')
    ax.set_title('Pareto Chart of Effects', fontsize=14)
    ax.set_xlabel('Absolute Effect', fontsize=12)
    ax.set_ylabel('Coefficients', fontsize=12)
    ax.grid(axis='x')

    # Adjust layout to make sure labels fit
    plt.tight_layout(pad=2.0)  # Add padding to the layout

    # Embed the plot in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, white_box1)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to plot Y vs X1 and Y vs X2 in the top left white box
def plot_effects(coefficients):
    # Calculate Y values for X1 and X2
    X1_values = np.array([-1, 1])  # Points for X1
    X2_values = np.array([-1, 1])  # Points for X2


    # Calculate Y for X1 (X2 = 0)
    Y_X1 = calculate_Y(coefficients, X1_values, 0)
    #Y_X1 = coefficients[0] + coefficients[1] * X1_values + coefficients[2] * 0 + coefficients[3] * X1_values * 0

    # Calculate Y for X2 (X1 = 0)
    Y_X2 = calculate_Y(coefficients, 0, X2_values)
    #Y_X2 = coefficients[0] + coefficients[1] * 0 + coefficients[2] * X2_values + coefficients[3] * 0 * X2_values

    # Clear the previous plots
    for widget in white_box3.winfo_children():
        widget.destroy()

    # Create a new figure for the combined plot
    fig, axs = plt.subplots(1, 2, figsize=(5, 2), sharey=True)  # 1 row, 2 columns, sharing Y-axis

    # Plot Y vs X1
    axs[0].plot(X1_values, Y_X1, 'o-', color='blue')
    axs[0].set_title('Y vs X1 (X2=0)')
    axs[0].set_xlabel('X1')
    axs[0].set_ylabel('Y')
    axs[0].set_xticks(X1_values)  # Set X ticks to show -1 and 1
    axs[0].grid()

    # Plot Y vs X2
    axs[1].plot(X2_values, Y_X2, 'o-', color='blue')
    axs[1].set_title('Y vs X2 (X1=0)')
    axs[1].set_xlabel('X2')
    axs[1].set_ylabel('Y')
    axs[1].set_xticks(X2_values)  # Set X ticks to show -1 and 1
    axs[1].grid()

    # Set the same Y-axis limits for both plots
    max_y = max(max(Y_X1), max(Y_X2))
    min_y = min(min(Y_X1), min(Y_X2))
    axs[0].set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))
    axs[1].set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))

    # Show the plots in white_box
    canvas = FigureCanvasTkAgg(fig, master=white_box3)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to plot the lines Y(-1,-1) to Y(-1,1) and Y(1,-1) to Y(1,1)
def plot_lines(coefficients):

    # Calculate Y values for X1 and X2
    X1_values = np.array([-1, 1])  # Points for X1
    X2_values = np.array([-1, 1])  # Points for X2


    # Calculate Y for X1,X2
    Y_X11 = calculate_Y(coefficients, X1_values, -1)
    Y_X12 = calculate_Y(coefficients, X1_values, 1)
    Y_X21 = calculate_Y(coefficients, -1, X2_values)
    Y_X22 = calculate_Y(coefficients, 1, X2_values)
    
    # Clear the previous plots 
    for widget in white_box2.winfo_children():
        widget.destroy()

    # Create a new figure for the combined plot
    fig, axs = plt.subplots(1, 2, figsize=(5, 2), sharey=True)  # 1 row, 2 columns, sharing Y-axis

    # Plot Y vs X1
    axs[0].plot(X1_values, Y_X11, 'o-', color='blue')
    axs[0].plot(X1_values, Y_X12, 'o-', color='green')
    axs[0].set_title('Y vs X1 (X2=0)')
    axs[0].set_xlabel('X1')
    axs[0].set_ylabel('Y')
    axs[0].set_xticks(X1_values)  # Set X ticks to show -1 and 1
    axs[0].grid()

    # Plot Y vs X2
    axs[1].plot(X2_values, Y_X21, 'o-', color='blue')
    axs[1].plot(X2_values, Y_X22, 'o-', color='green')
    axs[1].set_title('Y vs X2 (X1=0)')
    axs[1].set_xlabel('X2')
    axs[1].set_ylabel('Y')
    axs[1].set_xticks(X2_values)  # Set X ticks to show -1 and 1
    axs[1].grid()

    # Set the same Y-axis limits for both plots
    max_y = max(max(Y_X11),max(Y_X12), max(Y_X21), max(Y_X22))
    min_y = min(min(Y_X11),min(Y_X12),min(Y_X21), min(Y_X22))
    axs[0].set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))
    axs[1].set_ylim(min_y-0.1*(max_y-min_y), max_y+0.1*(max_y-min_y))

    # Show the plots 
    canvas = FigureCanvasTkAgg(fig, white_box2)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Function to handle button click and display the equation
def on_calculate():
    try:
        # Get input values for Y
        Y_values = [float(entry.get()) for entry in entries_Y]
        Y = np.array(Y_values)
        
        # Calculate coefficients
        global coefficients  # Declare coefficients as global to access in plot_effects
        coefficients = calculate_coefficients(Y, X1, X2)
        
        # Display the equation
        equation = f"Y = {coefficients[0]:.2f} + {coefficients[1]:.2f} * X1 + {coefficients[2]:.2f} * X2 + {coefficients[3]:.2f} * X1 * X2"
        equation_label.config(text=equation)
        
        # Plot the Pareto chart in white_box3
        plot_pareto_chart(coefficients)
        
        # Plot Y vs X1 and Y vs X2 in white_box1
        plot_effects(coefficients)
        
        # Plot the lines in white_box2
        plot_lines(coefficients)
        
    except ValueError:
        equation_label.config(text="Please enter valid numeric values for Y.")

# Given values for X1 and X2
X1 = np.array([-1, 1, -1, 1])
X2 = np.array([-1, -1, 1, 1])

# Default Y values
default_Y_values = [1, 2, 3, 8]

# Calculate coefficients before setting up the GUI
Y = np.array(default_Y_values)
coefficients = calculate_coefficients(Y, X1, X2)

# Create the main window
root = tk.Tk()
root.title("Calculate Equation Coefficients")

# Create labels and entry widgets for X1, X2, and Y values in a table format
entries_Y = []

tk.Label(root, text="X1", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="X2", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Y", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5)

for i in range(4):
    tk.Label(root, text=f"{X1[i]}", font=("Arial", 12)).grid(row=i+1, column=0, padx=10, pady=5)
    tk.Label(root, text=f"{X2[i]}", font=("Arial", 12)).grid(row=i+1, column=1, padx=10, pady=5)
    
    entry_Y = tk.Entry(root, width=10, font=("Arial", 12))
    entry_Y.grid(row=i+1, column=2, padx=10, pady=5)
    entry_Y.insert(0, str(default_Y_values[i]))  # Set default value for Y
    entries_Y.append(entry_Y)

# Create a button to calculate the equation
button = tk.Button(root, text="Calculate", command=on_calculate, font=("Arial", 12))
button.grid(row=5, columnspan=3, pady=10)

# Label to display the final equation inside a black box
equation_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="white", width=40)
equation_label.grid(row=6, columnspan=3, padx=10, pady=10)

# Create two additional white boxes
white_box1 = tk.Label(root, bg="white", width=70, height=20)  # Right of the input table
white_box1.grid(row=0, column=3, rowspan=7, padx=10, pady=10)

white_box2 = tk.Label(root, bg="white", width=70, height=20)  # Right of the Pareto chart
white_box2.grid(row=7, column=3, padx=10, pady=10)

# Create an additional white box under the input table for the Pareto chart
white_box3 = tk.Label(root, bg="white", width=70, height=20)  # Under the input table
white_box3.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

# Display the equation using the pre-calculated coefficients
equation = f"Y = {coefficients[0]:.2f} + {coefficients[1]:.2f} * X1 + {coefficients[2]:.2f} * X2 + {coefficients[3]:.2f} * X1 * X2"
equation_label.config(text=equation)

# Plot the Pareto chart and effects using the pre-calculated coefficients
plot_pareto_chart(coefficients)
plot_effects(coefficients)
plot_lines(coefficients)

# Run the GUI event loop
root.mainloop()
