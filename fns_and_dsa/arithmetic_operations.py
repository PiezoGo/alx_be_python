def perform_operation(num1,num2,operation):
    if operation == 'add':
        sum = num1+num2
    elif operation == 'subtract':
        sum = num1-num2
    elif operation == 'multiply':
        sum = num1*num2
    elif operation == 'divide':
        if num2 != 0:
            sum = num1/num2
        else:
            print("You are attempting to divide by 0!!")
    else:
        print("Please enter a valid operation!")
    return sum


