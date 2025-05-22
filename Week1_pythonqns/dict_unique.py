dict = {
    'a': [1, 2, 3],
    'b': [2, 3, 4],
    'c': [4, 5, 6]
}
seen= []
for key in dict:
    unique= []
    for value in dict[key]:
        if value not in seen:
            unique.append(value)
            seen.append(value)
    dict[key]= unique

print(dict)
