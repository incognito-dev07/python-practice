# Calculator Program

operator = input("Enter an operator (+ - * /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = "null"

if operator == "+":
  result = num1 + num2
elif operator == "-":
  result = num1 - num2
elif operator == "*":
  result = num1 * num2
elif operator == "/":
  if num2 == 0:
    print("0 is an invalid divisor")
  else:
    result = num1 / num2
else:
  print("Invalid operator")
  
print(f"\nResult: {result}")