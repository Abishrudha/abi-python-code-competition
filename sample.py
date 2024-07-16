print("select operations")
print("1.add")
print("2.Subtract")
print("3.multi")
print("4.Divide")

choice = input("enter choice (1,2,3,4) :")

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

if choice == '1':
  total = num1 + num2
  print(total)
elif choice == '2':
  print(num1 - num2)
elif choice == '3':
  multi = num1 * num2
  print(multi)
elif choice == '4':
  divide = num1 / num2
  print(divide)
else:
  print("invalid input")