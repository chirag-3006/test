a=float(input("enter first number: "))
b=float(input("enter second number: "))
operator=input("enter operator: ")

match operator:
    case "+":
        result=a+b
        print("reult:", result)

    case "-":
        result=a-b
        print("result:", result)
    case "*":
        result=a*b
        print("result:", result)

    case "/":
        result=a/b
        print("result:", result)
    case "%":
        
        result=a%b
        print("result:", result)

    case _:
        print("invalid operator")