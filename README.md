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

## Collision resolution by chaining

---

Make our array of slots into an array of linked lists.
Each linked list node is a HashTableEntry.

## Put

SlotIndex Chain (linked list)

---

0 -> None
1 HashTableEntry("foo", 12) -> None
2 HashTableEntry("baz", 999) -> HashTableEntry("bar", 50) -> None
3 -> None

put("foo", 12) #hashes to 1
put("bar", 30) #hashes to 2
put("baz", 999) #hashes to 2 -- collision
put("bar", 50) #hashes to 2 -- collision

1. Figure out the index
2. Search the linked list to see if the key is there
   2a. If the key is there, overwrite the value
   2b. if not there, create a new HashTableEntry and insert it in the list

## Get

1. Figure out the index for the key
2. Search the linked list at theindex for the HashTableEntry that matches the key
3. Return the value for the entry, or None if not found

## Delete

1. Figure out the index for the key
2. Search the linked list at the index for the HashTAbleEntry that matches the key
   2a. If found, delete the entry from the linked list -- return the value
   2b. If not found, return None

## Hash table load factor

Metric to indicate how overfull the hashtable is.
<br>
O(1) hash table:
0 |-> D
1 |-> H
2 |-> A
3 |-> C
4 |-> G
5 |-> B
6 |-> E
7 |-> F

0 |-> D -> M
1 |-> H
2 |-> A -> I
3 |-> C -> J -> L - N
4 |-> G
5 |-> B -> O
6 |-> E -> K -> P
7 |-> F

How do we know when to resize the hash table?
load factor = number of elements stored in the hash table / number of slots.

4 / 8 = 0.5
8 / 8 = 1.0
18 / 8 = 2.0

If the load factor is over 0.7, grow the table.
If the load factor is under 0.2, shrink the table (down to some minimum)
Grow the table: double the size
Shrink the table: halve the size

When you PUT:
---if the load factor > 0.7:
------create a new array with double the sie of the old one
------for each element i the old array:
---------PUT rehash all elements into new array
