# input() takes whatever the user types as text (a string).
# int() converts that text into an integer (whole number).
num1 = int(input("Enter the first number: "))

# Ask the user for another number and convert the input from a string into an integer.
num2 = int(input("Enter the second number: "))


# A function is a reusable block of code.
# num1 and num2 inside the brackets are called PARAMETERS.
# Parameters are values that the function expects to receive.
def add(num1, num2):
    result = num1 + num2
    print("The sum of", num1, "and", num2, "is:", result)


def subtract(num1, num2):
    result = num1 - num2
    print("The difference of", num1, "and", num2, "is:", result)


def multiply():
    result = num1 * num2
    print("The product of", num1, "and", num2, "is:", result)


def divide(num1, num2):

    # % is the modulus operator.
    # It gives the remainder after dividing num1 by num2.
    result = num1 % num2

    # f"" is called an f-string (formatted string).
    # Anything inside { } is evaluated by Python and inserted into the text.
    print(f"The remainder of {num1} and {num2} is {result}.")


# Call (run) each function.
# The values of num1 and num2 are passed to the function as arguments.
add(num1, num2)
subtract(num1, num2)
multiply()
divide(num1, num2)