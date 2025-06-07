import math

while True:
    print("\n--- Simple Calculator ---")
    print("1. Square Root")
    print("2. Power (x^y)")
    print("3. sin, cos, tan")
    print("4. Log and Log10")
    print("5. Factorial")
    print("6. GCD")
    print("7. LCM (Python 3.9+)")
    print("8. Hypotenuse")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        num = float(input("Enter a number: "))
        print("Square root is:", math.sqrt(num))

    elif choice == "2":
        x = float(input("Enter base number: "))
        y = float(input("Enter power: "))
        print("Result is:", math.pow(x, y))

    elif choice == "3":
        angle = float(input("Enter angle in degrees: "))
        rad = math.radians(angle)
        print("sin =", math.sin(rad))
        print("cos =", math.cos(rad))
        print("tan =", math.tan(rad))

    elif choice == "4":
        num = float(input("Enter number > 0: "))
        print("log =", math.log(num))
        print("log10 =", math.log10(num))

    elif choice == "5":
        n = int(input("Enter a whole number: "))
        print("Factorial is:", math.factorial(n))

    elif choice == "6":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("GCD is:", math.gcd(a, b))

    elif choice == "7":
        if hasattr(math, 'lcm'):
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM is:", math.lcm(a, b))
        else:
            print("Your Python version does not support LCM")

    elif choice == "8":
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        print("Hypotenuse is:", math.hypot(a, b))

    elif choice == "9":
        print("Goodbye Atharv! 👋")
        break

    else:
        print("Invalid choice. Try again.")
