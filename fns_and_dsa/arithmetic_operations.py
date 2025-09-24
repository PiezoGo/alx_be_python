def perform_operation(num1,num2,operation):
    if operation == 'add':
        soln=num1+num2
    elif operation == 'subtract':
        soln=num1-num2
    elif operation == 'multiply':
        soln=num1*num2
    elif operation == 'divide':
        if num2 == 0:
            raise ZeroDivisionError("You are attempting to divide by 0!!")
        else:
            soln=num1/num2

    else:
        print("Please enter a valid operation!")
    return soln


from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()


