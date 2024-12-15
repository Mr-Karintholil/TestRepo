def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Welcome to the calculator!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"4 * 7 = {multiply(4, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")
