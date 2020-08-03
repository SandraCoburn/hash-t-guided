# Hash Tables

---

What do they solve?
Standard array search: 0(n)
Hash Table Search: O(1)

Main hash table operations: GET PUT DELETE

The mapping between an item and the slot the itme belogns is called a **hash function.**
The has function will take any item in the collection and return an integer in the range of slot names, between 0 and m-1.
One hash function is called the remainder method.
When presented with an item, the hash function is the item devided by the table size, this is then its slot number.
ex.:
-we preassign an empty hash table of m=11

- our remainder hash function then is:
  h(item)=item%11
  item - hash Value.
  54 % 11 = 10
  26 % 11 = 4
  93 % 11 = 5

'''
Non integer elements:
we can also crate hash functions for character based items such a string elements.
The word "cat" can be thought of as a sequence of ordinal values: ord("c"), ord("a"), ord("t")
c = 99
a = 97
t = 116
= 312 % 11 = 4
'''

In Python, we can encode strings into their bytes representation with the .encode() method. Once encoded, an integer represents each character.

# Collisions

When there is a collision and not fucntion to handle it, the hash function put will just overwrite the previous values
