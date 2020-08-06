#Dictionaries don't have a sorting system
#There is a way to get a touple with the keys and values
d = {
    "foo": 12,
    "bar": 17,
    "quick": 2
}
'''
for t in d.items():
    print(t)
'''

#There is a way to get a touple with the keys and values by puting them in a list
items = list(d.items())
items.sort() #you can sort by key but not value
#reverse sorting
items.sort(reverse=True)
print(items)

#sorting by value by passing a  function
def valsort(e):
    return e[1]
items.sort(key=valsort)
print(items)

#using an anonimus function Lambda and does the same thing as above
items.sort(key=lambda e: e[1])
print(items)