num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

res = num1 + num2
'''
print("The sum of", num1, "and", num2, "is:", sum)
print("The product of", num1, "and", num2, "is", num1*num2,".")
print(f"The reminder of {num1} and {num2} is {num1 / num2}.")
print("The difference of", num1, "and", num2, "is", str(num1 - num2) + ".")
'''

# making functions

def sum():
    print("The sum of", num1, "and", num2, "is:", res)

def min():
    print("The difference of", num1, "and", num2, "is", str(num1 - num2) + ".")

def prd():
    print("The product of", num1, "and", num2, "is", num1*num2,".")

def div():
    print(f"The reminder of {num1} and {num2} is {num1 / num2}.")


sum()