def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def main():
    print("Welcome to the my Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4): "))
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == 1:
            print(f"Result: {add(num1, num2)}")
        elif choice == 2:
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 3:
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 4:
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
          break

    print("Thank you for using the  Calculator!")

if  __name__== "__main__":
    main()
