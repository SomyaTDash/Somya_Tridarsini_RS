lst= ["abc", "def", ["ghi", "jkl"]]
res= []
for x in lst:
    if type(x) == list:
        for y in x:
            res.extend(list(y))
    else:
        res.extend(list(x))
print(res)
