a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

operation = input("enterany operation you want to performe(+,-,*,/)")

match operation:
    case '+':
        print(f"Sum of {a} and {b}={a+b}")
    case '-':
        print(f"substraction of {a} and {b}={a-b}")
        
    case '*':
        print(f"Sum of {a} and {b}={a*b}")
    case '/':
        if(b==0):
            print("B cant not be Zero in division")
        else:
            print(f"Division of {a} and {b}={a/b}")
