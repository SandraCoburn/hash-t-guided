HASH_DATA_SIZE = 8
hash_data = [0] * HASH_DATA_SIZE
#This function will look for the byte code of input
def hash_function(s):
    """ Naive hashing funciton -- do not use in production"""
    bytes_list = s.encode()
    #bytes_list = str(s).encode() this will take of numbers if they're gonna be used as a key
    total = 0

    for b in bytes_list: #O(n) over the length of the key not the hash data, O(1) over the Hash data table       
        total += b
    return total
    #total &= oxffffff #force it to 32 bit (8 f's)
    #total &= 0xffffffffffffffff #32 bit (19f's)

def get_index(s):
    hash_value = hash_function(s)
    return hash_value % HASH_DATA_SIZE

def put(k,v):
    #For a given key, store a value in that hash table
    index = get_index(k)
    hash_data[index] = v

def get(k):
    #for a given key return the value
    index = get_index(k)
    return hash_data[index]

print(hash_data)
index = get_index("Sandra!")
# hash_data[index] = "Hello, World!"
put("hello", "hello, world")
put("Sandra1", "Sandra!")
print(hash_data)
print(get("Sandra1"))



print(hash_function("Sandra!") % HASH_DATA_SIZE)
print(get_index("Sandra!"))
print(hash_function("House"))