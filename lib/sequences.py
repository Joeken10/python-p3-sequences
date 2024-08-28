#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])  # Return an empty list for non-positive lengths
        return
    
    if n == 1:
        print([0])  # Return only the first Fibonacci number
        return

    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
   
