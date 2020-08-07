l = [1,2,3,4,5,1,2,3,4,5,7,1,1,2,4,3,8] * 10
ht = {}
print("Building hash table:")
#By building the hashtable we reduce the time complexity in the is_in_list function
for x in l: #O(n)
    ht[x] = True
def is_in_list(n):
    '''for x in l:
        if n == x:
            return True
    return False'''
    return n in ht # O(1)
print(is_in_list(3))
for i in range(10):
    print(is_in_list(i))
