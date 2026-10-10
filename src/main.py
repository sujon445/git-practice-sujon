from datetime import date
from utils import add, subtract, multiply

print("Name: Md Shohel Rana Sujon")
print("Today's Date:", date.today())

from datetime import date
from utils import add, subtract, multiply

print("Name: Md Shohel Rana Sujon")
print("Today's Date:", date.today())

try:
    a = float(input("Md Shohel Rana: "))
    b = float(input("Sujon: "))

    print("Addition:", add(a, b))
    print("Subtraction:", subtract(a, b))
    print("Multiplication:", multiply(a, b))

except ValueError:
    print("Error: Please enter valid numbers.")

except TypeError as error:
    print("Error:", error)