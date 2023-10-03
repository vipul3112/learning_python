a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
print('+ for addition')
print('- for substraction')
print('* for multiplication')
print('/ for divide')
print('% for modulus')
c=input("")
match c:
        case '+':
                print(a+b)
        case '-':
          print(a-b) # no brake; statement is used in python
        case '*':
          print(a*b)
        case '/':
          print(a/b)
        case '%':
          print(a%b)
        case _:
          print("Enter valid operator")
          
