# first Python program
import time

def add(x, y):
    return x + y

def subtract (x, y):
    return x - y

def multiply (x, y):
    return x * y

def divide (x, y):
    return x / y

print("Select Operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit Program")

choice = input('Which operation: (1, 2, 3, 4, 5)? ')
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    if num2 == 0:
        print("Undefined")
    else:
        print(num1, "/", num2, "=", divide(num1, num2))

elif choice == '5':
    print("Goodbye.")

else:
    print("Invalid Input")

time.sleep(3)
exit()