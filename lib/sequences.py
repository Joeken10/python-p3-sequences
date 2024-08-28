#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])  # Return an empty list for non-positive lengths
        return
    
    if n == 1:
        print([0])  # Return only the first Fibonacci number
        return
