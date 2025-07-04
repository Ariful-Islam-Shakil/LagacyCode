from tabulate import tabulate  # External package, install with: pip install tabulate
from typing import List, Tuple

def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtracts one number from another.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a - b

def multiply(a: float, b: float) -> float:
    """
    Multiplies two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.

    Raises:
        TypeError: If a or b is not a number.
    """
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides one number by another.

    Args:
        a (float): The dividend.
        b (float): The divisor.

    Returns:
        float: The quotient of a and b.

    Raises:
        ValueError: If b is zero.
        TypeError: If a or b is not a number.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b  # Python 3 ensures float division

def display_results_as_table(a: float, b: float) -> None:
    """
    Displays the results of various operations as a table.

    Args:
        a (float): The first number.
        b (float): The second number.
    """
    results: List[List[str]] = [
        ["Operation", "Result"],
        ["Addition", str(add(a, b))],
        ["Subtraction", str(subtract(a, b))],
        ["Multiplication", str(multiply(a, b))],
        ["Division", str(divide(a, b))]
    ]
    print(tabulate(results, headers="firstrow", tablefmt="grid"))

def main() -> None:
    """
    The main function.

    Performs calculations on two numbers and displays the results as a table.
    """
    a: float = 10
    b: float = 5
    print(f"Performing calculations on {a} and {b}")
    try:
        display_results_as_table(a, b)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()