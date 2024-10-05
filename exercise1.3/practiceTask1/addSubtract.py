number = int(input("Type a number: "))
number2 = int(input("Type another number: "))
operator = input("Choose '+' or '-' ")

if operator ==  '+':
  print(number, "+", number2, "=", str(number + number2))

elif operator == '-':
  print(number, "-", number2, "=", str(number - number2))

else:
  print("Unknown operator")