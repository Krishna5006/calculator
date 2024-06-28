print(r''' _____________________
|  _________________  |
| | Krishna      0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')

def add (x,y):
  return x+y

def subtraction (x,y):
  return x-y

def multiplication (x,y):
  return x*y

def division (x,y):
  return x/y



def calculator(first_num):
  print("+")
  print("-")
  print("*")
  print("/")
  operation=input("Pick an operation: ")
  second_num=float(input("Enter II number: "))

  if operation == "+":
    result=add(first_num,second_num)
  
  elif operation == "-":
    result=subtraction(first_num,second_num)
  
  elif operation == "*":
    result=multiplication(first_num,second_num)
  
  elif operation == "/":
    result=division(first_num,second_num)
  
  else:
    return "Invalid Operation"
  
  print(f"{first_num} {operation} {second_num} = {result}")
  
  next=input(f"Type 'Y' to continue calculating with {result},type 'N' to start a new calculation or any letter to end the calculation:  ")
  if next == "Y":
    calculator(result)
  elif next == "N":
    calculator(float(input("Enter a no: ")))
  else:
    print("")
  
calculator(float(input("Enter a no: ")))