while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("0. Exit")

    user_Choice = int(input("Enter your choice: "))

    if user_Choice == 1:
        print("ADDITION")
        num1 = int(input("Enter a Number:"))
        num2 = int(input("Enter another Number:"))
        print(add(num1, num2))

    elif user_Choice == 2:
        print("SUBTRACT")
        num1 = int(input("Enter a Number:"))
        num2 = int(input("Enter another Number:"))
        print(sub(num1, num2))

    elif user_Choice == 3:
        print("MULTIPLY")
        num1 = int(input("Enter a Number:"))
        num2 = int(input("Enter another Number:"))
        print(multi(num1, num2))

    elif user_Choice == 4:
        print("DIVISION")
        num1 = int(input("Enter a Number:"))
        num2 = int(input("Enter another Number:"))
        print(div(num1, num2))

    elif user_Choice == 0:
        print("Goodbye")
        break


    else:
        print("There is no such input as: ",user_Choice)

        # functions for calculator

        def add(a, b):
            return a + b


        def sub(a, b):
            return a - b


        def multi(a, b):
            return a * b


        def div(a, b):
            return a / b
