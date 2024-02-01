# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/31/2024
# Description: Project 4b

def fib(nterms):
    n1, n2 = 1, 1
    count = 2  # Start with count=2 to account for the first two terms

    while count < nterms:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

    return n2  # Return n2, which contains the nth Fibonacci number