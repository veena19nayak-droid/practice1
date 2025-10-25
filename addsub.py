#math.py
try:
   a=float(input("Enter first number:"))
   b=float(input("Enter second number:"))

   print(f"Addtion: {a+b}")
   print(f"Subtraction: {a-b}")
except ValueError:
   print("Please enter valid numbers.")
