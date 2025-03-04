class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Error! Division by zero.")
        return x / y

    def calculate(self, operation, x, y):
        if operation == 'add':
            return self.add(x, y)
        elif operation == 'subtract':
            return self.subtract(x, y)
        elif operation == 'multiply':
            return self.multiply(x, y)
        elif operation == 'divide':
            return self.divide(x, y)
        else:
            raise ValueError("Invalid operation")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    calculator = Calculator()
    print("Welcome to the Premium Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            operation_map = {
                '1': 'add',
                '2': 'subtract',
                '3': 'multiply',
                '4': 'divide'
            }

            operation = operation_map[choice]
            try:
                result = calculator.calculate(operation, num1, num2)
                print(f"The result of {operation}ing {1} and {2} is: {result}")
            except ValueError as e:
                print(e)

        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    main()