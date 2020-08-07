import math
lookup_table = {}
'''We can buil up the table first before the function or inside the function'''
# for i in range(1, 1001):
#     lookup_table[i] = 1/math.sqrt(i)
def inv_sqrt(n):
    '''n is an integer between 1 and 1000'''
    #Lazily build lookup table
    if n not in lookup_table:
        lookup_table[n] = 1/math.sqrt(n)
    # return 1 / math.sqrt(n)
    return lookup_table[n]
print(inv_sqrt(10))
print(inv_sqrt(100))