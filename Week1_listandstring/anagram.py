a= "listen"
b= "silent"
if len(a)!= len(b):
    print(False)
else:
    d={}
    for c in a:
        d[c]= d.get(c, 0) + 1
    for c in b:
        if c not in d or d[c] == 0:
            print(False)
            break
        d[c]-= 1
    else:
        print(True)
