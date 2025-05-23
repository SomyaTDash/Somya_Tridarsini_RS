s= "aaabbcccc"
e= ""
i= 0
while i < len(s):
    c= 1
    while i +1< len(s) and s[i]== s[i +1]:
        c+= 1
        i+= 1
    if c>= 3:
        e+= s[i] + str(c)
    else:
        e+= s[i] * c
    i+= 1
print(e)
