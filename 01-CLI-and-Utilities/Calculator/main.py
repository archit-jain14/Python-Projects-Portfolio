a=int(input("Enter first number: "))
b=(input("Enter any arithmetic operator:"))
c=int(input("Enter second number: "))
if b== "+" :
  print("The output is:",a+c)
elif b== "-" :
  print("The output is:",a-c)
elif b== "*" :
  print("The output is:",a*c)
elif b== "/" :
  print("The output is:",a/b)
else:
  print("Invalid operator")