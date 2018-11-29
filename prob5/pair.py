## Problem 5 of Daily Programming Problems
### This problem was asked by Jane Street
#
#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
#
#Given this implementation of cons:
#
#def cons(a, b):
#    def pair(f):
#        return f(a, b)
#    return pair
#
#Implement car and cdr.

def f(a, b):
    return a, b

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

""" car(pair) returns first number of the pair
"""
def car(f):
    def first(a, b):
        return a
    return f(first)

""" car(pair) returns second number of the pair
"""
def cdr(f):
    def second(a, b):
        return b
    return f(second)

def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))

if __name__ == "__main__":
    main()