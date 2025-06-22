from typing import Optional
from tabulate import tabulate  # External package that must be installed

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> Optional[float]:
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def display_results_as_table(a: int, b: int) -> None:
    results = [
        ["Operation", "Result"],
        ["Addition", add(a, b)],
        ["Subtraction", subtract(a, b)],
        ["Multiplication", multiply(a, b)],
        ["Division", divide(a, b)]
    ]
    print(tabulate(results, headers="firstrow", tablefmt="grid"))

def main() -> None:
    a = 10
    b = 5
    print(f"Performing calculations on {a} and {b}")
    try:
        display_results_as_table(a, b)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
