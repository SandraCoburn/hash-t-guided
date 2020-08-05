#Fibonacci sequence
#0,1,1,2,3,5,8,13,34
'''
def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2) #runtime O(2n) it will compute every single number over and over

for i in range(100):
    print(f"{i:3}: {fib(i)}")
'''
#Better runtime if you cache the calculations once so the computer won't do it again

cache = {} #O(n)
def fib(n):
    if n<= 1:
        return n
    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2) #it will save the calculcations in cache so it won't do it again
    return cache[n]

for i in range(100):
    print(f"{i:3}: {fib(i)}")

'''You can add a cache with two parameters too:'''
cache = {} #O(n)
def abc(x,y):

    if (x,y) not in cache:
        cache[x,y] = fib(n-1) + fib(n-2) #it will save the calculcations in cache so it won't do it again
    return cache[x,y]