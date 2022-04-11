"""
hw10.py

Problem: This program defines a number of functions relating to while loops and their applications
         within functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

# from graphics import *

def fibonacci(n):
    if n < 1:
        return None

    first_val = 0  # initialized at zero, since this makes n==1 and n==2 return the same value (1)
    second_val = 1
    count = 1  # initialized at one, since all n less than one returns None
    while count < n:
        sum_both = first_val + second_val
        first_val = second_val  # increments left-hand number up the chain of values
        second_val = sum_both  # same as above, but  right-hand number

        count += 1
    return second_val

def double_investment(principle, rate):
    investment_val = principle
    apr = 1 + rate
    years_invested = 0
    while investment_val < (principle * 2):
        investment_val = investment_val * apr
        years_invested += 1
    return years_invested

def syracuse(n):
    val_lst = [n]
    while not n == 1:
        if n % 2 == 0:
            n /= 2
            val_lst.append(n)
        else:
            n = 3 * n + 1
            val_lst.append(n)
    return val_lst


def is_prime(n):
    test_divisor = n - 1
    while test_divisor > 1:
        if n % test_divisor == 0:
            return False
        test_divisor -= 1
    return True


def is_odd(n):
    return n % 2 == 1

def goldbach(n):
    if is_odd(n) or n < 2:  # rejects non-Goldbach input
        return None

    # since only (odd + odd) results in  even, list initialized as the smallest ten odd primes
    lst_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    # appends to lst_primes the 10 largest primes that are smaller than n
    count_2 = n - 1
    while len(lst_primes) < 20:
        if is_odd(count_2) and is_prime(count_2):
            lst_primes.append(count_2)
        count_2 -= 1

    # checks the sum of each number against every possible combination. inefficient, but works.
    # first checks sum of lst_primes[0] and every other number, then lst_primes[1], etc.
    output = []
    first_pos = 0  # first_pos == position of num checked against all else
    while first_pos < len(lst_primes) - 1:
        second_pos = len(lst_primes) - 1
        while second_pos >= 0:
            if lst_primes[first_pos] + lst_primes[second_pos] == n:
                output.append(lst_primes[first_pos])
                output.append(lst_primes[second_pos])
                # ↓ ugly way to force while loops to break
                first_pos = 1000
                second_pos = -1000
            second_pos -= 1
        first_pos += 1
    return output
