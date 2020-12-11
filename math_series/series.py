

# # Ask user input
# """User instructions/ask user for params (n,first_num,second_num);
# n is required and others optional"""

# def welcome():
#     print("""\n** Welcome we will ask for 1 to 3 positive integers to generate
#     the nth place in either a Fibonacci, Lucas, or random series **\n""")

# def determine_params ():

#     print (""" \n** Please enter a positive integer **
#     to see the value of that place in the series **\n """)
#     n = input('  > ')

#     print ("""\n ** Do you wish to enter other parameters (yes/no)? 
#     If no, a Fibonnacci series number will be generated. **\n""")

#     more = input('  > ')


#     if more.lower() == 'yes' or more.lower() == 'y':
#         print ("""\n ** Please enter 0 to see the Fibonacci number or **
#         2 to see the Lucas or any positive integer to see a random series **\n """)
#         first_num = input('  > ')
        
#         print ("""\n ** Please enter 1 to see the Fibonacci or Lucas number or
#         any positive integer to see a random series **\n """)
#         second_num = input('  > ')
#     else:
#         first_num = 0
#         second_num = 1  

#     return n,first_num,second_num


# # Create Fibonacci function
# """Calculates a Fibonacci series to nth place if params are (n,0,1) or (n)"""

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


    # print(f" {fib_series[n]} is at place {n} in the Fibonacci series")
    return fib_series[n-1]


# # Create Lucas function
# """Calculates a Lucas series up to nth place if user params are (n,2,1)"""

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



    # print(f" {luc_series[n]} is at place {n} in the Lucas series")
    return luc_series[n-1]

# Create random function
"""Calculates random series to nth place if params are (n,x,y) for any x,y"""

def sum_series (n,a=0,b=1):
    x = 0
    sum_series_list = [a,b]
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for x in range(2,(n+1)):
            sum_next = sum_series_list[x-1]+ sum_series_list[x-2]
            sum_series_list.append(sum_next)


    # print(f"{sum_series_list[n]} is at place {n} in your series")
    return sum_series(n)

# # function calls in main; use 'ifs' to call based on user input
# """Main function calls others and produces output"""

# def main():
#     # Global variables
#     n = 0
#     first_num = 0
#     second_num = 0

#     welcome()
#     determine_params()
    
#     print(n,first_num,second_num)

#     if first_num == 0 and second_num == 1:
#         fibonnaci(n,first_num,second_num)
#     elif first_num == 2 and second_num == 1:
#         lucas(n,first_num,second_num)
#     else:
#         sum_series(n,first_num,second_num)
        
# # # execution

# main()