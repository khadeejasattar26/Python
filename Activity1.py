
def factorial(n):
    #calculating factorial
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
#user is giving input
number = int(input("Enter a number to calculate its factorial: "))

#to check that either the given num is negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
  #calculating factorial
    result = factorial(number)
    #printing factorial3
    print("Factorial of", number, "is", result)
