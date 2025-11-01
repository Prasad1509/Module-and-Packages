Day 1:
Ex1:
import math

print("Value of pi is:", math.pi)
print("Value of e is:", math.e)
print("Square root of 25 is:",math.sqrt(34))
print("cos(0):", math.cos(0))     
print("sin(0):", math.sin(0))      
print("tan(0):", math.tan(0))
print("Degrees to radians:", math.radians(180))  
print("Radians to degrees:", math.degrees(math.pi))
print("e raised to 2 is:", math.exp(2))
print("log base e of 10:", math.log(10))       
print("log base 10 of 100:", math.log10(100))

print("math.floor(3.7):", math.floor(3.7))  
print("math.ceil(3.2):", math.ceil(3.2))

Ex2:
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
        b = int(input("Enter second
        
