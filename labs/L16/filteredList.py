from math import sqrt,ceil

def drop_divisible(n,lst):
    return ([item for item in lst if item%n != 0 or n == item])
    

def sieve_with(candidates, lst):
    for c in candidates:
        lst=drop_divisible(c,lst)
    return lst

def sieve(n):
    return sieve_with(range(2,ceil(sqrt(n))+1), range(2,n))