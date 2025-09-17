num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result=num1+num2
    case "-":
        result=num1-num2
    case "*":
        result=num1*num2
    case "/":
        if num2 == 0:
            print("You are trying to divide by 0!!")
        else:
            result = num1/num2
    case _:
        print("please enter a valid operation")

print(f"The result is {result}")
