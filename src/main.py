from datetime import date
from utils import add, subtract, multiply

print("Name: Md Shohel Rana Sujon")
print("Today's Date:", date.today())

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")

except TypeError as error:
    print("Error:", error)