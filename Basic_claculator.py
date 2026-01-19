while True:
    # options 
    print("\n1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Modulus")

    choice = int(input("Select an option: "))

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    # Logic
    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero")

    elif choice == 5:
        print("Result:", num1 % num2)

    else:
        print("Invalid option")

    # for asking start again
    again = input("\nDo you want to perform another task? (y/n): ").lower()
    if again != "y":
        print("Calculator closed.")
        break
    else:
        print("Start again")
