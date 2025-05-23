lst=[('a', 1), ('b', 2), ('a', 3)]
result= {}
for key,value in lst:
    if key in result:
        result[key].append(value)
    else:
        result[key]= [value]
print(result)
