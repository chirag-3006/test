a=float(input("enter first number: "))
b=float(input("enter second number: "))
operator=input("enter operator: ")

match operator:
    case "+":
        result = a + b
        print("Result:", result)

    case "-":
        result = a - b
        print("Result:", result)
    case "*":
        result = a * b
        print("Result:", result)

    case "/":
        result = a / b
        print("Result:", result)
    case "%":
        
        result = a % b
        print("Result:", result)

    case _:
        print("Invalid operator")