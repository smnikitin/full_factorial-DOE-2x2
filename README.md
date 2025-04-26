# Calculate Equation Coefficients

This repository contains a Python application that calculates the coefficients of a linear equation based on user-provided Y values and plots the effects using Tkinter and Matplotlib.

## Features

- **Calculate Coefficients**: Computes the coefficients of the equation `Y = a + b*X1 + c*X2 + d*X1*X2` based on user input.
- **Pareto Chart**: Plots a Pareto chart of the effects of the coefficients.
- **Effect Plots**: Displays plots of `Y` vs `X1` and `Y` vs `X2`.
- **Interactive GUI**: Provides an interactive GUI for input and visualization using Tkinter.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3. Install the required dependencies:
    ```bash
    pip install numpy matplotlib tkinter
    ```

## Usage

1. Run the application:
    ```bash
    python your_script_name.py
    ```
2. Enter the Y values in the provided input fields.
3. Click the "Calculate" button to compute the coefficients and display the plots.

## Code Overview

### `calculate_coefficients(Y, X1, X2)`

Calculates the coefficients of the linear equation based on the input Y values and the given X1 and X2 values.

### `plot_pareto_chart(coefficients, master)`

Plots a Pareto chart of the effects of the coefficients.

### `plot_effects(coefficients)`

Displays plots of `Y` vs `X1` and `Y` vs `X2`.

### `on_calculate()`

Handles the button click event to calculate the coefficients and update the plots.

## GUI Layout

- **Input Table**: Allows users to input Y values corresponding to given X1 and X2 values.
- **Equation Display**: Shows the calculated equation.
- **Pareto Chart**: Displays the Pareto chart of effects.
- **Effect Plots**: Shows the plots of `Y` vs `X1` and `Y` vs `X2`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact [your-email@example.com](mailto
