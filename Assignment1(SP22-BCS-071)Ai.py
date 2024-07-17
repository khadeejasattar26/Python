def fibonacci_series(num_terms):
#initializing first 2 terms
    a, b = 0, 1
    series = [a, b]

    for _ in range(2, num_terms):
        a, b = b, a + b #update values of a and b
        series += [b] #add next term to series

    return series
#taking the imput for number of terms
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

fib_series = fibonacci_series(num_terms)

print("Fibonacci series up to {} terms:".format(num_terms), end=" ")
for term in fib_series:
    print("{}".format(term), end=" ")
