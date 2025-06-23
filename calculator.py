from tabulate import tabulate  # External package, install with: pip install tabulate

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return float(a) / b  # Ensure float division

def display_results_as_table(a, b):
    results = [
        ["Operation", "Result"],
        ["Addition", add(a, b)],
        ["Subtraction", subtract(a, b)],
        ["Multiplication", multiply(a, b)],
        ["Division", divide(a, b)]
    ]
    print tabulate(results, headers="firstrow", tablefmt="grid")

def main():
    a = 10
    b = 5
    print "Performing calculations on {} and {}".format(a, b)
    try:
        display_results_as_table(a, b)
    except ValueError as e:
        print "Error: {}".format(e)

if __name__ == "__main__":
    main()
