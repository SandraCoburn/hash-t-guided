def letter_count(s):
    d = {}
    for c in s:
        if c.isspace(): #ignore spaces
            continue
        c = c.lower() #to lower cases
        if c not in d:
            d[c] = 0
        d[c] += 1
    print(d)
    return d
letter_count("Hello")

def print_sorted_letter_count(s):
    d = letter_count(s)

    items = list(d.items())

    items.sort(key=lambda e: e[1], reverse=True)
    for i in items:
        print(f"{i[0]}: {i[1]}")
print_sorted_letter_count("They also thought in the 1080s that therew would be flying cars")