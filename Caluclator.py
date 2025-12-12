def add(a, b):
    c = a + b
    print("Result:", c)

def sub(a, b):
    c = a - b
    print("Result:", c)

def mul(a, b):
    c = a * b
    print("Result:", c)

def div(a, b):
    c = a / b
    print("Result:", c)

def power(a, b):
    c = a ** b
    print("Result:", c)

def percent(a, b):
    c = (a / b) * 100
    print("Result:", c)

def square(a):
    c = a * a
    print("Result:", c)

def square_root(a):
    if a < 0:
        print("Invalid input. Please enter a positive number to compute the square root.")
    else:
        c = a ** 0.5
        print("Result:", c)

def cube(a):
    c = a ** 3
    print("Result:", c)


def main():
    print("\nWelcome! You are using a Python Calculator")
    print("-------------------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. x^y (Power)")
    print("6. Percentage (a out of b)")
    print("7. Square")
    print("8. Square Root")
    print("9. Cube")
    print("10. Exit")
    print("-------------------------------------------")

    while True:
        try:
            choice = int(input("\nEnter your choice (1–10): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 10:
            print("Thank you for using the calculator. Goodbye.")
            break

        try:
            a = float(input("Enter first number: "))
            if choice in [1, 2, 3, 4, 5, 6]:
                b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input,please enter valid input")
            continue


        if choice == 1:
            add(a, b)
        elif choice == 2:
            sub(a, b)
        elif choice == 3:
            mul(a, b)
        elif choice == 4:
            div(a, b)
        elif choice == 5:
            power(a, b)
        elif choice == 6:
            percent(a, b)
        elif choice == 7:
            square(a)
        elif choice == 8:
            square_root(a)
        elif choice == 9:
            cube(a)
        else:
            print("Invalid choice. Select a number between 1 and 10.")
            continue

        continuation_choice = input("\nDo you want to continue? (yes/no): ").lower()
        if continuation_choice == "yes":
            print("Continuing...")
        elif continuation_choice == "no":
            print("BYE, SEE YOU SOON")
            break
        else:
            print("Invalid input,enter valid inputs")
            


if __name__ == "__main__":
    main()
