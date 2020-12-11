

# Ask user input
# In re-reading the instructions, I chose to do testing vs CLI input

# Create Fibonacci function
"""Calculates a Fibonacci series to nth place if params are (n,0,1) or (n)"""

def fibonacci(n):
    x = 0
    fib_series = [0,1]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for x in range(2,(n+1)):
            fib_next = fib_series[x-1]+ fib_series[x-2]
            fib_series.append(fib_next)

    return fib_series[n-1]


# Create Lucas function
"""Calculates a Lucas series up to nth place if user params are (n,2,1)"""

def lucas(n):
    x = 0
    luc_series = [2,1]
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        for x in range(2,(n+1)):
            luc_next = luc_series[x-1]+ luc_series[x-2]
            luc_series.append(luc_next)

    return luc_series[n-1]

# Create random function
"""Calculates random series to nth place if params are (n,x,y) for any x,y"""

def sum_series (n,a=7,b=9):
    x = 0
    series = [a,b]

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for x in range(2,(n+1)):
            sum_next = series[x-1]+ series[x-2]
            series.append(sum_next)

    return series[n-1]

