#Define the function needed: add, sub, mul, div
#Print option to the user
#Ask for values
#Call the function
#While loop to continue the program until the user want to exit

#lets start
print("***Welcome To Our Calculator***")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")
# Addition
def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + "=" + str(answer))
# Subtraction
def sub(a,b):
    answer = a-b
    print(str(a) + "-" + str(b) + "=" + str(answer))
# Multiply
def mul(a,b):
    answer = a*b
    print(str(a) + "*" + str(b) + "=" + str(answer))

# Division
def div(a,b):
    answer = a/b
    print(str(a) + "/" + str(b) + "=" + str(answer))

choice = input("Input your choice:")
# Addition
if choice == "a" or choice =="A":
    print("Addition")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    add(a,b)
# Subtraction
elif choice == "b" or choice =="B":
    print("Subtration")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sub(a,b)
# Multiplication
elif choice == "c" or choice =="C":
    print("Multiplication")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    mul(a,b)
# Division
elif choice == "d" or choice =="D":
    print("Division")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    div(a,b)
# Exit
elif choice == "e" or choice =="E":
    print("program ended")
    quit()
else:
    print("Invalid operation")
